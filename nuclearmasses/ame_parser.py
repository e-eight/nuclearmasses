import numpy as np
import pandas as pd

from nuclearmasses.ame_formats import AME_MASS_FORMAT, AME_RCT1_FORMAT, AME_RCT2_FORMAT
from nuclearmasses.parser import ELEMENTS, FWFParser

AME_YEARS = [1993, 1995, 2003, 2012, 2016, 2020]


class AMEMassParser(FWFParser):
    """Parses AME mass files."""

    def __init__(self, year: int):
        if year not in AME_YEARS:
            raise ValueError(f"You must choose a year from {AME_YEARS}.")
        self.year = year

    def _colspecs(self) -> dict[str, tuple[int, int]]:
        if self.year == 2020:
            return AME_MASS_FORMAT["2020"]
        if 2003 <= self.year <= 2016:
            return AME_MASS_FORMAT["2003"]
        if self.year <= 1995:
            return AME_MASS_FORMAT["1993"]

    def _filespecs(self) -> dict[str, int]:
        if self.year == 2020:
            return {"header": 35, "footer": 0}
        if 2003 <= self.year <= 2016:
            return {"header": 38, "footer": 0}
        if self.year <= 1995:
            return {"header": 39, "footer": 0}

    def _sanitize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        to_float = [
            col for col in df.columns if col not in ["Z", "A", "BetaDecayChannel"]
        ]
        for col in to_float:
            if "Error" not in col:
                df[col + "Extrapolated"] = df[col].str.endswith("#")
        df = df.replace("#", ".0", regex=True)
        df = df.replace("*", np.nan)
        df["AtomicMass"] = df["AtomicMass"].replace(" ", "", regex=True)
        df[to_float] = df[to_float].apply(pd.to_numeric, errors="coerce")
        if self.year <= 1995:
            df["BindingEnergyPerNucleon"] = df["BindingEnergy"] / df["A"]
            df["BindingEnergyPerNucleonError"] = df["BindingEnergyError"] / df["A"]

        df["N"] = df["A"] - df["Z"]
        df["Symbol"] = [ELEMENTS[z] for z in df["Z"]]
        df["TableYear"] = self.year

        return df


class AMEReactionParser(FWFParser):
    """Parses AME reaction files."""

    def __init__(self, year: int, rct: int):
        if year not in AME_YEARS:
            raise ValueError(f"You must choose a year from {AME_YEARS}.")
        self.year = year
        if rct != 1 and rct != 2:
            raise ValueError("rct must be either 1 or 2.")
        self.rct = rct
        self.rct_format = AME_RCT1_FORMAT if self.rct == 1 else AME_RCT2_FORMAT

    def _colspecs(self) -> dict[str, tuple[int, int]]:
        if self.year == 2020:
            return self.rct_format["2020"]
        if self.year < 2020:
            return self.rct_format["1993"]

    def _filespecs(self) -> dict[str, int]:
        if self.year == 2020:
            header = 35 if self.rct == 1 else 37
            footer = 0 if self.rct == 1 else 15
            return {"header": header, "footer": footer}
        if self.year < 2020:
            return {"header": 39, "footer": 0}

    def _sanitize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # The 2020 reaction 2 dataset repeats the row containing column names after
        # every few rows which needs to be removed
        if self.year == 2020 and self.rct == 2:
            idx = df[df["A"].str.contains("A")].index
            df = df.drop(idx)
            df["A"] = df["A"].astype(int)
            df["Z"] = df["Z"].astype(int)
        to_float = [col for col in df.columns if col not in ["Z", "A"]]
        for col in to_float:
            if "Error" not in col:
                df[col + "Extrapolated"] = df[col].str.endswith("#")
        df = df.replace("#", ".0", regex=True)
        df = df.replace("*", np.nan)
        df[to_float] = df[to_float].apply(pd.to_numeric, errors="coerce")

        df["N"] = df["A"] - df["Z"]
        df["Symbol"] = [ELEMENTS[z] for z in df["Z"]]
        df["TableYear"] = self.year

        return df
