import pandas as pd

from nuclearmasses.nubase_formats import NUBASE_FORMAT
from nuclearmasses.parser import ELEMENTS, FWFParser

NUBASE_YEARS = [2003, 2012, 2016, 2020]


class NUBASEParser(FWFParser):
    """Parses NUBASE files."""

    def __init__(self, year: int):
        if year not in NUBASE_YEARS:
            raise ValueError(f"You must choose a year from {NUBASE_YEARS}.")
        self.year = year

    def _colspecs(self) -> dict[str, tuple[int, int]]:
        if self.year == 2020:
            return NUBASE_FORMAT["2020"]
        if 2012 <= self.year <= 2016:
            return NUBASE_FORMAT["2012"]
        if self.year == 2003:
            return NUBASE_FORMAT["2003"]

    def _filespecs(self) -> dict[str, int]:
        if self.year == 2020:
            return {"header": 25, "footer": 0}
        if self.year < 2020:
            return {"header": 0, "footer": 0}

    def _sanitize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        isospin_pattern = r"T=(\d[\/\d]*)"
        df["Isospin"] = df["SpinParity"].str.extract(isospin_pattern)
        df["Spin"] = df["SpinParity"].str.replace(isospin_pattern, "", regex=True)

        for col in ["NUBASEMassExcess", "ExcitationEnergy"]:
            df[col + "Extrapolated"] = df[col].str.endswith("#")
            df[col] = df[col].replace("#$", ".0", regex=True)
            df[col] = df[col].apply(pd.to_numeric, errors="coerce")
            df[col + "Error"] = df[col + "Error"].apply(pd.to_numeric, errors="coerce")

        df["N"] = df["A"] - df["Z"]
        # Extract decay channels
        df["Decay"] = df["Decay"].fillna("UNKNOWN")
        df["Decay"] = df["Decay"].str.split(";", n=1).str[0]
        df["Decay"] = df["Decay"].str.split("=| |~|<|>", n=1).str[0]
        df["Decay"] = df["Decay"].replace({"e+": "B+", "IS": "stable"})
        # 198Au has a typo in it's decay mode in the 2012 table. It is recorded as '-'.
        if self.year == 2012:
            df.loc[(df["A"] == 198) & (df["Z"] == 79), "Decay"] = "B-"
        df["Symbol"] = [ELEMENTS[z] for z in df["Z"]]
        df["TableYear"] = self.year

        return df
