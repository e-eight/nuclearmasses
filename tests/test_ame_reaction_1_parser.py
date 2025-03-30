import importlib.resources

from nuclearmasses.ame_parser import AMEReactionParser


def test_ame_reaction_1_parser():
    data_dir = importlib.resources.files("nuclearmasses.data")

    year = 1993
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1_rmd.mas93")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15618.44
    assert ir186["TwoNeutronSeparationEnergyError"] == 270.74
    assert ir186["TwoProtonSeparationEnergy"] == 9522.98
    assert ir186["TwoProtonSeparationEnergyError"] == 20.49
    assert ir186["QAlpha"] == 3852.98
    assert ir186["QAlphaError"] == 103.94
    assert ir186["QTwoBeta"] == -7419.61
    assert ir186["QTwoBetaError"] == 145.57
    assert ir186["QEpsilon"] == -2635.85
    assert ir186["QEpsilonError"] == 20.03
    assert ir186["QBetaNeutron"] == -10622.0
    assert ir186["QBetaNeutronError"] == 230.0

    year = 1995
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1_rmd.mas95")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15618.41
    assert ir186["TwoNeutronSeparationEnergyError"] == 270.74
    assert ir186["TwoProtonSeparationEnergy"] == 9522.89
    assert ir186["TwoProtonSeparationEnergyError"] == 20.49
    assert ir186["QAlpha"] == 3853.04
    assert ir186["QAlphaError"] == 103.94
    assert ir186["QTwoBeta"] == -7495.33
    assert ir186["QTwoBetaError"] == 145.56
    assert ir186["QEpsilon"] == -2635.83
    assert ir186["QEpsilonError"] == 20.03
    assert ir186["QBetaNeutron"] == -10682.0
    assert ir186["QBetaNeutronError"] == 207.6

    year = 2003
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1.mas03")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15704.74
    assert ir186["TwoNeutronSeparationEnergyError"] == 32.47
    assert ir186["TwoProtonSeparationEnergy"] == 9524.26
    assert ir186["TwoProtonSeparationEnergyError"] == 17.08
    assert ir186["QAlpha"] == 3849.65
    assert ir186["QAlphaError"] == 103.31
    assert ir186["QTwoBeta"] == -7458.10
    assert ir186["QTwoBetaError"] == 26.70
    assert ir186["QEpsilon"] == -2639.77
    assert ir186["QEpsilonError"] == 16.57
    assert ir186["QBetaNeutron"] == -10561.10
    assert ir186["QBetaNeutronError"] == 44.19

    year = 2012
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1.mas12")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15706.55
    assert ir186["TwoNeutronSeparationEnergyError"] == 32.47
    assert ir186["TwoProtonSeparationEnergy"] == 9527.99
    assert ir186["TwoProtonSeparationEnergyError"] == 17.09
    assert ir186["QAlpha"] == 3848.03
    assert ir186["QAlphaError"] == 103.31
    assert ir186["QTwoBeta"] == -7459.92
    assert ir186["QTwoBetaError"] == 26.70
    assert ir186["QEpsilon"] == -2641.13
    assert ir186["QEpsilonError"] == 16.57
    assert ir186["QBetaNeutron"] == -10557.95
    assert ir186["QBetaNeutronError"] == 30.67

    year = 2016
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1-16.txt")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15704.13
    assert ir186["TwoNeutronSeparationEnergyError"] == 32.47
    assert ir186["TwoProtonSeparationEnergy"] == 9530.65
    assert ir186["TwoProtonSeparationEnergyError"] == 17.07
    assert ir186["QAlpha"] == 3848.80
    assert ir186["QAlphaError"] == 103.31
    assert ir186["QTwoBeta"] == -7457.49
    assert ir186["QTwoBetaError"] == 26.70
    assert ir186["QEpsilon"] == -2642.29
    assert ir186["QEpsilonError"] == 16.55
    assert ir186["QBetaNeutron"] == -10555.52
    assert ir186["QBetaNeutronError"] == 30.67

    year = 2020
    df = AMEReactionParser(year, 1).read_file(data_dir / str(year) / "rct1.mas20")
    _, ir186 = (
        df.loc[df["A"].eq(186) & df["Z"].eq(77)].to_dict(orient="index").popitem()
    )
    assert ir186["N"] == 109
    assert ir186["TwoNeutronSeparationEnergy"] == 15704.1312
    assert ir186["TwoNeutronSeparationEnergyError"] == 32.4655
    assert ir186["TwoProtonSeparationEnergy"] == 9530.4731
    assert ir186["TwoProtonSeparationEnergyError"] == 17.0698
    assert ir186["QAlpha"] == 3848.8777
    assert ir186["QAlphaError"] == 103.3133
    assert ir186["QTwoBeta"] == -7457.4943
    assert ir186["QTwoBetaError"] == 26.6968
    assert ir186["QEpsilon"] == -2642.2739
    assert ir186["QEpsilonError"] == 16.5459
    assert ir186["QBetaNeutron"] == -10555.5245
    assert ir186["QBetaNeutronError"] == 30.6658
