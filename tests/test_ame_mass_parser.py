import importlib.resources

from nuclearmasses.ame_parser import AMEMassParser


def test_ame_mass_parser():
    data_dir = importlib.resources.files("nuclearmasses.data")

    year = 1993
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass_rmd.mas93")

    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()
    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -46574.693
    assert iron67["AMEMassExcessError"] == 465.747
    assert iron67["BindingEnergy"] == 567012.139
    assert iron67["BindingEnergyError"] == 465.747
    assert iron67["BetaDecayEnergy"] == 8746.727
    assert iron67["BetaDecayEnergyError"] == 543.15
    assert iron67["AtomicMass"] == 66950000.0
    assert iron67["AtomicMassError"] == 500.0

    year = 1995
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass_rmd.mas95")

    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()
    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -46574.693
    assert iron67["AMEMassExcessError"] == 465.747
    assert iron67["BindingEnergy"] == 567012.133
    assert iron67["BindingEnergyError"] == 465.747
    assert iron67["BetaDecayEnergy"] == 8746.727
    assert iron67["BetaDecayEnergyError"] == 543.15
    assert iron67["AtomicMass"] == 66950000.0
    assert iron67["AtomicMassError"] == 500.0

    year = 2003
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass.mas03")

    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()

    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -45692.348
    assert iron67["AMEMassExcessError"] == 415.570
    assert iron67["BindingEnergyPerNucleon"] == 8449.695
    assert iron67["BindingEnergyPerNucleonError"] == 6.203
    assert iron67["BetaDecayEnergy"] == 9368.702
    assert iron67["BetaDecayEnergyError"] == 523.438
    assert iron67["AtomicMass"] == 66950947.244
    assert iron67["AtomicMassError"] == 446.132

    year = 2012
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass.mas12")
    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()

    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -46068.530
    assert iron67["AMEMassExcessError"] == 217.972
    assert iron67["BindingEnergyPerNucleon"] == 8455.310
    assert iron67["BindingEnergyPerNucleonError"] == 3.253
    assert iron67["BetaDecayEnergy"] == 9253.245
    assert iron67["BetaDecayEnergyError"] == 218.067
    assert iron67["AtomicMass"] == 66950543.395
    assert iron67["AtomicMassError"] == 234.002

    year = 2016
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass16.txt")
    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()

    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -45610.155
    assert iron67["AMEMassExcessError"] == 270.285
    assert iron67["BindingEnergyPerNucleon"] == 8448.469
    assert iron67["BindingEnergyPerNucleonError"] == 4.034
    assert iron67["BetaDecayEnergy"] == 9711.620
    assert iron67["BetaDecayEnergyError"] == 270.362
    assert iron67["AtomicMass"] == 66951035.482
    assert iron67["AtomicMassError"] == 290.163

    year = 2020
    df = AMEMassParser(year).read_file(data_dir / str(year) / "mass.mas20")
    _, iron67 = df.query("A == 67 and Z == 26").to_dict(orient="index").popitem()

    assert iron67["N"] == 41
    assert iron67["Symbol"] == "Fe"
    assert iron67["AMEMassExcess"] == -45708.416
    assert iron67["AMEMassExcessError"] == 3.819
    assert iron67["BindingEnergyPerNucleon"] == 8449.9359
    assert iron67["BindingEnergyPerNucleonError"] == 0.0570
    assert iron67["BetaDecayEnergy"] == 9613.3678
    assert iron67["BetaDecayEnergyError"] == 7.4900
    assert iron67["AtomicMass"] == 66950930.00
    assert iron67["AtomicMassError"] == 4.100
