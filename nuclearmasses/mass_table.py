"""Functionality to parse all data file into a single object."""

import importlib.resources
import logging
import pathlib
import typing

import pandas as pd

from nuclearmasses.ame_parser import AME_YEARS, AMEMassParser, AMEReactionParser
from nuclearmasses.nubase_parser import NUBASE_YEARS, NUBASEParser


def ame_data(year: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    AME mass and reaction datasets for the specified year.

    The datasets are obtained from https://www-nds.iaea.org/amdc/. Atomic masses and
    corresponding errors are in micro u. Mass excess, binding energies, Q-values, and
    corresponding errors are in keV.

    In the original text files, extrapolated values are indicated by a `#` at the end
    of the number. For example, the mass excess value for 3Li in the 2003 dataset is
    `28667#` (keV). Here the `#`s have been removed. Instead an additional column
    `MassExcessExtrapolated` indicates if the corresponding `MassExcess` value has been
    obtained from extrapolation. Columns for atomic masses, binding energies, and
    Q-values have been similarly processed.

    Parameters:
    -----------
    year : int
        The AME year. See https://www-nds.iaea.org/amdc/ for valid years. Currently
        contains all datasets up to 2020.

    Returns:
    --------
    mass_df : pd.DataFrame
        Atomic masses dataset from year.
    rct1_df : pd.DataFrame
        Reaction energies, table 1 dataset from year.
    rct2_df : pd.DataFrame
        Reaction energies, table 2 dataset from year.
    """
    if year not in AME_YEARS:
        raise ValueError(f"You must choose a year from {AME_YEARS}")

    data_dir = importlib.resources.files("nuclearmasses.data") / str(year)

    match year:
        case 1993:
            mass_file = data_dir / "mass_rmd.mas93"
            rct1_file = data_dir / "rct1_rmd.mas93"
            rct2_file = data_dir / "rct2_rmd.mas93"
        case 1995:
            mass_file = data_dir / "mass_rmd.mas95"
            rct1_file = data_dir / "rct1_rmd.mas95"
            rct2_file = data_dir / "rct2_rmd.mas95"
        case 2003:
            mass_file = data_dir / "mass.mas03"
            rct1_file = data_dir / "rct1.mas03"
            rct2_file = data_dir / "rct2.mas03"
        case 2012:
            mass_file = data_dir / "mass.mas12"
            rct1_file = data_dir / "rct1.mas12"
            rct2_file = data_dir / "rct2.mas12"
        case 2016:
            mass_file = data_dir / "mass16.txt"
            rct1_file = data_dir / "rct1-16.txt"
            rct2_file = data_dir / "rct2-16.txt"
        case 2020:
            mass_file = data_dir / "mass.mas20"
            rct1_file = data_dir / "rct1.mas20"
            rct2_file = data_dir / "rct2.mas20"

    mass_df = AMEMassParser(year).read_file(mass_file)
    rct1_df = AMEReactionParser(year, 1).read_file(rct1_file)
    rct2_df = AMEReactionParser(year, 2).read_file(rct2_file)
    return mass_df, rct1_df, rct2_df


def nubase_data(year: int) -> pd.DataFrame:
    """
    NUBASE dataset for the specified year.

    The datasets are obtained from https://www-nds.iaea.org/amdc/. Mass excess and
    isomer excitation energies are in keV. Extrapolated mass excess and isomer excitation
    energies are indicated by the `MassExcessExtrapolated` and
    `ExcitationEnergyExtrapolated` columns, respectively. For more information on
    extrapolated data, see `ame_data`.

    Spin and parity information are provided in the `SpinParity` column. Besides
    extracting isospin values into a separate `Isospin` column, these aren't processed.
    Similarly, half-life or decay string information aren't processed. See the associated
    NUBASE publications listed on https://www-nds.iaea.org/amdc/ for more information
    about these columns.

    Parameters:
    -----------
    year : int
        The Nubase year. See https://www-nds.iaea.org/amdc/ for valid years. Currently
        contains all datasets up to 2020.

    Returns:
    --------
    nubase_df : pd.DataFrame
        NUBASE dataset from year.
    """
    if year not in NUBASE_YEARS:
        raise ValueError(f"You must choose a year from {NUBASE_YEARS}")

    data_dir = importlib.resources.files("nuclearmasses.data") / str(year)

    match year:
        case 2003:
            nubase_file = data_dir / "nubtab03.asc"
        case 2012:
            nubase_file = data_dir / "nubtab12.asc"
        case 2016:
            nubase_file = data_dir / "nubase2016.txt"
        case 2020:
            nubase_file = data_dir / "nubase_1.mas20"

    nubase_df = NUBASEParser(year).read_file(nubase_file)
    return nubase_df


class MassTable:
    """Storage class for all of the mass data.

    Internally there are separate dataframes for the NUBASE and AME data as well as a
    combined one for all data
    """

    def __init__(self):
        """Do all of the work at construction."""
        self.data_path = importlib.resources.files("nuclearmasses.data")
        self.nubase = pd.concat(
            [nubase_data(y) for y in NUBASE_YEARS], ignore_index=True
        )
        self.ame = pd.concat(
            [self._combine_ame_data(y) for y in AME_YEARS], ignore_index=True
        )
        self.full_data = self._combine_all_data()
        self._do_indexing()

    def _combine_ame_data(self, year: int) -> pd.DataFrame:
        """Combine all the AME files from the given year into a Pandas DataFrame."""
        mass_df, rct1_df, rct2_df = ame_data(year)

        # Merge all 3 of the AME files/data frames into one
        common_columns = ["A", "Z", "N", "TableYear", "Symbol"]
        merged_df = mass_df.merge(rct1_df, on=common_columns, how="outer").merge(
            rct2_df, on=common_columns, how="outer"
        )
        return merged_df

    def _combine_all_data(self) -> pd.DataFrame:
        """Combine all NUBASE and AME data into a Pandas DataFrame."""
        common_columns = ["A", "Z", "N", "TableYear", "Symbol"]
        df = self.nubase.merge(self.ame, on=common_columns, how="outer")

        df["NUBASERelativeError"] = abs(
            df["NUBASEMassExcessError"] / df["NUBASEMassExcess"]
        )
        df["AMERelativeError"] = abs(df["AMEMassExcessError"] / df["AMEMassExcess"])

        # 12C has a 0.0 +/ 0.0 mass excess by definition so calculating relative error -> NaN
        # Set the value to 0.0 as that's what it is
        df.loc[(df.Symbol == "C") & (df.A == 12), "NUBASERelativeError"] = 0.0
        df.loc[(df.Symbol == "C") & (df.A == 12), "AMERelativeError"] = 0.0
        return df

    def _do_indexing(self) -> None:
        """
        Set the index of the DataFrames to the table year. This is done in place so
        nothing is returned.
        """
        self.nubase.set_index("TableYear", inplace=True)
        self.ame.set_index("TableYear", inplace=True)
        self.full_data.set_index("TableYear", inplace=True)
