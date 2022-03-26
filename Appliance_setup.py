#! /usr/bin/env python3

from Appliance import EnergySupplier, Toaster, Vacuum, Fridge, Oven

edf_std = EnergySupplier(EnergySupplier.supplier_dict["EDF"]["standard"])
tim_toaster = Toaster()
vera_vacuum = Vacuum()
frosty_fridge = Fridge()
olga_oven = Oven()

print(tim_toaster)
print("Using energy supplied by", tim_toaster.get_energy_supplier())
print(tim_toaster.calculate_cost(hours=1))

print("_" * 30)
print(vera_vacuum)
print("Using Energy Supplied by: ", vera_vacuum.get_energy_supplier())
print(vera_vacuum.calculate_cost(hours=1))
print("")

print("_" * 30)
print(frosty_fridge)
print("Using Energy Supplied by: ", frosty_fridge.get_energy_supplier())
print(frosty_fridge.calculate_cost(hours=1))
print("")

print("_" * 30)
print(olga_oven)
print("Using Energy Supplied by: ", olga_oven.get_energy_supplier())
print(olga_oven.calculate_cost(hours=1))
print("")
