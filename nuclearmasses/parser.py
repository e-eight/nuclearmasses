from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class FWFParser(ABC):
    """Abstract class for parsing nuclear data files in fixed width format."""

    def __init__(self):
        super().__init__()

    @abstractmethod
    def _colspecs(self) -> dict[str, tuple[int, int]]:
        """
        Specifies the names and extents of the fixed-width fields of each line.

        The keys of the returned dictionary are the names of the fields. The values are
        the half-open intervals specifying the extents of the fields.
        """
        raise NotImplementedError

    @abstractmethod
    def _filespecs(self) -> dict[str, int]:
        """
        Specifies if any number of rows must be skipped from the top or bottom of
        a data file.

        The returned dictionary must return values for the following keys:
        - `header` which specifies the number of rows to be skipped from the top,
        - `footer` which specifies the number of rows to be skipped from the bottom.
        If no rows are to be the skipped from the top or the bottom then these values
        must be 0.
        """
        raise NotImplementedError

    @abstractmethod
    def _sanitize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the DataFrame so that it can be used for further data analysis.

        Parameters:
        -----------
        df : DataFrame
            The DataFrame to clean.

        Returns:
        --------
        The cleaned DataFrame.
        """
        raise NotImplementedError

    def read_file(self, file: Path | str) -> pd.DataFrame:
        """
        Creates a DataFrame from the specified file. This method should not be used
        directly. Instead use one of the functions, such as `ame_data`, or
        `nubase_data`, from `nuclearmasses.py`.

        Parameters:
        -----------
        file : Path, or str
            The file containing the data. Must be in a fixed width format.

        Returns:
        --------
        A DataFrame containing selected data from the file. The selection depends on
        the `self._colspecs` implementation.
        """
        colspecs = self._colspecs()
        df = pd.read_fwf(
            file,
            colspecs=list(colspecs.values()),
            skiprows=self._filespecs()["header"],
            skipfooter=self._filespecs()["footer"],
        )
        df.columns = list(colspecs.keys())

        return self._sanitize_data(df)


ELEMENTS = [
    "n",
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
    "Sc",
    "Ti",
    "V",
    "Cr",
    "Mn",
    "Fe",
    "Co",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Y",
    "Zr",
    "Nb",
    "Mo",
    "Tc",
    "Ru",
    "Rh",
    "Pd",
    "Ag",
    "Cd",
    "In",
    "Sn",
    "Sb",
    "Te",
    "I",
    "Xe",
    "Cs",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Pm",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Ho",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "W",
    "Re",
    "Os",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "Po",
    "At",
    "Rn",
    "Fr",
    "Ra",
    "Ac",
    "Th",
    "Pa",
    "U",
    "Np",
    "Pu",
    "Am",
    "Cm",
    "Bk",
    "Cf",
    "Es",
    "Fm",
    "Md",
    "No",
    "Lr",
    "Rf",
    "Db",
    "Sg",
    "Bh",
    "Hs",
    "Mt",
    "Ds",
    "Rg",
    "Cn",
    "Ed",
    "Fl",
    "Ef",
    "Lv",
    "Ts",
    "Og",
]
