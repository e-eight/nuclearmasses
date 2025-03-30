import importlib.resources
from pandas.testing import assert_frame_equal
from nuclearmasses.mass_table import ame_data, nubase_data
from nuclearmasses.ame_parser import AMEMassParser, AMEReactionParser
from nuclearmasses.nubase_parser import NUBASEParser


def test_ame_data():
    data_dir = importlib.resources.files("nuclearmasses.data")
    
    # 1993
    year = 1993
    mass_df, rct1_df, rct2_df = ame_data(year)

    data_path = data_dir / str(year)
    mass_df_alt = AMEMassParser(year).read_file(data_path / "mass_rmd.mas93")
    rct1_df_alt = AMEReactionParser(year, 1).read_file(data_path / "rct1_rmd.mas93")
    rct2_df_alt = AMEReactionParser(year, 2).read_file(data_path / "rct2_rmd.mas93")

    assert_frame_equal(mass_df, mass_df_alt)
    assert_frame_equal(rct1_df, rct1_df_alt)
    assert_frame_equal(rct2_df, rct2_df_alt)

    # 2016
    year = 2016
    mass_df, rct1_df, rct2_df = ame_data(year)

    data_path = data_dir / str(year)
    mass_df_alt = AMEMassParser(year).read_file(data_path / "mass16.txt")
    rct1_df_alt = AMEReactionParser(year, 1).read_file(data_path / "rct1-16.txt")
    rct2_df_alt = AMEReactionParser(year, 2).read_file(data_path / "rct2-16.txt")

    assert_frame_equal(mass_df, mass_df_alt)
    assert_frame_equal(rct1_df, rct1_df_alt)
    assert_frame_equal(rct2_df, rct2_df_alt)

    # 2020
    year = 2020
    mass_df, rct1_df, rct2_df = ame_data(year)

    data_path = data_dir / str(year)
    mass_df_alt = AMEMassParser(year).read_file(data_path / "mass.mas20")
    rct1_df_alt = AMEReactionParser(year, 1).read_file(data_path / "rct1.mas20")
    rct2_df_alt = AMEReactionParser(year, 2).read_file(data_path / "rct2.mas20")

    assert_frame_equal(mass_df, mass_df_alt)
    assert_frame_equal(rct1_df, rct1_df_alt)
    assert_frame_equal(rct2_df, rct2_df_alt)


def test_nubase_data():
    data_dir = importlib.resources.files("nuclearmasses.data")
    
    year = 2003
    nubase_df = nubase_data(year)
    nubase_df_alt = NUBASEParser(year).read_file(data_dir / str(year) / "nubtab03.asc")
    assert_frame_equal(nubase_df, nubase_df_alt)

    year = 2016
    nubase_df = nubase_data(year)
    nubase_df_alt = NUBASEParser(year).read_file(data_dir / str(year) / "nubase2016.txt")
    assert_frame_equal(nubase_df, nubase_df_alt)

    year = 2020
    nubase_df = nubase_data(year)
    nubase_df_alt = NUBASEParser(year).read_file(data_dir / str(year) / "nubase_1.mas20")
    assert_frame_equal(nubase_df, nubase_df_alt)
