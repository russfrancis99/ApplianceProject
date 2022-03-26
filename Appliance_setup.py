#! /usr/bin/env python3

from Appliance import EnergySupplier, Toaster, Vacuum, Fridge, Oven

edf_std = EnergySupplier(EnergySupplier.supplier_dict["EDF"]["standard"])
tim_toaster = Toaster()
vera_vacuum = Vacuum()
frosty_fridge = Fridge()
olga_oven = Oven()

print(tim_toaster)
print("Using energy supplied by", tim_toaster.get_energy_supplier())
print("Power Consumption: ", tim_toaster.get_power_consumption(), "kw/h")
print(tim_toaster.calculate_cost(hours=1))

print("_" * 30)
print(vera_vacuum)
print("")

print("_" * 30)
print(frosty_fridge)
print("")

print("_" * 30)
print(olga_oven)
