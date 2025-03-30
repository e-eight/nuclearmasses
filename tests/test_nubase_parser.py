import importlib.resources

from nuclearmasses.nubase_parser import NUBASEParser


def test_nubase():
    data_dir = importlib.resources.files("nuclearmasses.data")

    year = 2003
    df = NUBASEParser(year).read_file(data_dir / str(year) / "nubtab03.asc")
    _, cu57 = (
        df.query("A == 57 and Z == 29 and State == 0").to_dict(orient="index").popitem()
    )
    assert cu57["N"] == 28
    assert cu57["NUBASEMassExcess"] == -47310
    assert cu57["NUBASEMassExcessError"] == 16
    assert cu57["HalfLife"] == "196.3"
    assert cu57["HalfLifeUnit"] == "ms"
    assert cu57["HalfLifeError"] == "0.7"
    assert cu57["SpinParity"] == "3/2-"
    assert cu57["Decay"] == "B+"

    year = 2012
    df = NUBASEParser(year).read_file(data_dir / str(year) / "nubtab12.asc")

    # Select the ground state of 57Cu
    _, cu57 = (
        df.query("A == 57 and Z == 29 and State == 0").to_dict(orient="index").popitem()
    )
    assert cu57["N"] == 28
    assert cu57["NUBASEMassExcess"] == -47308.3
    assert cu57["NUBASEMassExcessError"] == 0.6
    assert cu57["HalfLife"] == "196.3"
    assert cu57["HalfLifeUnit"] == "ms"
    assert cu57["HalfLifeError"] == "0.7"
    assert cu57["SpinParity"] == "3/2-"
    assert cu57["DiscoveryYear"] == 1976
    assert cu57["Decay"] == "B+"

    year = 2016
    df = NUBASEParser(year).read_file(data_dir / str(year) / "nubase2016.txt")

    # Select the ground state of 57Cu
    _, cu57 = (
        df.query("A == 57 and Z == 29 and State == 0").to_dict(orient="index").popitem()
    )
    print(cu57)
    assert cu57["N"] == 28
    assert cu57["NUBASEMassExcess"] == -47308.9
    assert cu57["NUBASEMassExcessError"] == 0.5
    assert cu57["HalfLife"] == "196.3"
    assert cu57["HalfLifeUnit"] == "ms"
    assert cu57["HalfLifeError"] == "0.7"
    assert cu57["SpinParity"] == "3/2-"
    assert cu57["DiscoveryYear"] == 1976
    assert cu57["Decay"] == "B+"

    year = 2020
    df = NUBASEParser(year).read_file(data_dir / str(year) / "nubase_1.mas20")

    # Select the ground state of 57Cu
    _, cu57 = (
        df.query("A == 57 and Z == 29 and State == 0").to_dict(orient="index").popitem()
    )
    print(cu57)
    assert cu57["N"] == 28
    assert cu57["NUBASEMassExcess"] == -47309.0
    assert cu57["NUBASEMassExcessError"] == 0.5
    assert cu57["HalfLife"] == "196.4"
    assert cu57["HalfLifeUnit"] == "ms"
    assert cu57["HalfLifeError"] == "0.7"
    assert cu57["SpinParity"] == "3/2-*"
    assert cu57["ENDSFUpdateYear"] == 98
    assert cu57["DiscoveryYear"] == 1976
    assert cu57["Decay"] == "B+"
