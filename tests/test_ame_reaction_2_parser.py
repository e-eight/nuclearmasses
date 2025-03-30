import importlib.resources

from nuclearmasses.ame_parser import AMEReactionParser


def test_ame_reaction_2_parser():
    data_dir = importlib.resources.files("nuclearmasses.data")

    year = 1993
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2_rmd.mas93")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6655.82
    assert tl204["OneNeutronSeparationEnergyError"] == 0.29
    assert tl204["OneProtonSeparationEnergy"] == 6365.32
    assert tl204["OneProtonSeparationEnergyError"] == 1.26
    assert tl204["QFourBeta"] == -12492.85
    assert tl204["QFourBetaError"] == 71.39
    assert tl204["QDeuteronAlpha"] == 13712.87
    assert tl204["QDeuteronAlphaError"] == 1.23
    assert tl204["QProtonAlpha"] == 8183.14
    assert tl204["QProtonAlphaError"] == 1.25
    assert tl204["QNeutronAlpha"] == 7690.59
    assert tl204["QNeutronAlphaError"] == 15.05

    year = 1995
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2_rmd.mas95")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6655.86
    assert tl204["OneNeutronSeparationEnergyError"] == 0.29
    assert tl204["OneProtonSeparationEnergy"] == 6365.35
    assert tl204["OneProtonSeparationEnergyError"] == 1.26
    assert tl204["QFourBeta"] == -12494.05
    assert tl204["QFourBetaError"] == 92.85
    assert tl204["QDeuteronAlpha"] == 13713.05
    assert tl204["QDeuteronAlphaError"] == 1.23
    assert tl204["QProtonAlpha"] == 8183.32
    assert tl204["QProtonAlphaError"] == 1.24
    assert tl204["QNeutronAlpha"] == 7702.97
    assert tl204["QNeutronAlphaError"] == 3.35

    year = 2003
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2.mas03")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6656.10
    assert tl204["OneNeutronSeparationEnergyError"] == 0.29
    assert tl204["OneProtonSeparationEnergy"] == 6365.82
    assert tl204["OneProtonSeparationEnergyError"] == 1.25
    assert tl204["QFourBeta"] == -12470.66
    assert tl204["QFourBetaError"] == 24.01
    assert tl204["QDeuteronAlpha"] == 13710.69
    assert tl204["QDeuteronAlphaError"] == 1.15
    assert tl204["QProtonAlpha"] == 8181.34
    assert tl204["QProtonAlphaError"] == 1.16
    assert tl204["QNeutronAlpha"] == 7701.54
    assert tl204["QNeutronAlphaError"] == 3.34

    year = 2012
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2.mas12")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6656.09
    assert tl204["OneNeutronSeparationEnergyError"] == 0.29
    assert tl204["OneProtonSeparationEnergy"] == 6365.80
    assert tl204["OneProtonSeparationEnergyError"] == 1.25
    assert tl204["QFourBeta"] == -12470.19
    assert tl204["QFourBetaError"] == 22.31
    assert tl204["QDeuteronAlpha"] == 13710.68
    assert tl204["QDeuteronAlphaError"] == 1.14
    assert tl204["QProtonAlpha"] == 8181.16
    assert tl204["QProtonAlphaError"] == 1.15
    assert tl204["QNeutronAlpha"] == 7701.67
    assert tl204["QNeutronAlphaError"] == 3.33

    year = 2016
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2-16.txt")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6656.08
    assert tl204["OneNeutronSeparationEnergyError"] == 0.29
    assert tl204["OneProtonSeparationEnergy"] == 6365.85
    assert tl204["OneProtonSeparationEnergyError"] == 1.25
    assert tl204["QFourBeta"] == -12470.71
    assert tl204["QFourBetaError"] == 22.32
    assert tl204["QDeuteronAlpha"] == 13709.99
    assert tl204["QDeuteronAlphaError"] == 1.06
    assert tl204["QProtonAlpha"] == 8180.45
    assert tl204["QProtonAlphaError"] == 1.07
    assert tl204["QNeutronAlpha"] == 7700.97
    assert tl204["QNeutronAlphaError"] == 3.31

    year = 2020
    df = AMEReactionParser(year, 2).read_file(data_dir / str(year) / "rct2.mas20")
    _, tl204 = (
        df.loc[df["A"].eq(204) & df["Z"].eq(81)].to_dict(orient="index").popitem()
    )
    assert tl204["N"] == 123
    assert tl204["OneNeutronSeparationEnergy"] == 6656.0787
    assert tl204["OneNeutronSeparationEnergyError"] == 0.2907
    assert tl204["OneProtonSeparationEnergy"] == 6365.8379
    assert tl204["OneProtonSeparationEnergyError"] == 1.2542
    assert tl204["QFourBeta"] == -12470.8182
    assert tl204["QFourBetaError"] == 22.6974
    assert tl204["QDeuteronAlpha"] == 13710.0469
    assert tl204["QDeuteronAlphaError"] == 1.0612
    assert tl204["QProtonAlpha"] == 8180.5147
    assert tl204["QProtonAlphaError"] == 1.0721
    assert tl204["QNeutronAlpha"] == 7701.0380
    assert tl204["QNeutronAlphaError"] == 3.3084
