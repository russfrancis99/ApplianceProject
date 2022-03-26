#! /usr/bin/env python3

from Appliance import EnergySupplier, Toaster, Vacuum, Fridge, Oven

edf_std = EnergySupplier(EnergySupplier.supplier_dict["EDF"]["standard"])
tim_toaster = Toaster()
vera_vacuum = Vacuum()
frosty_fridge = Fridge()
olga_oven = Oven()

print(tim_toaster)
print(vera_vacuum)
print(frosty_fridge)
print(olga_oven)
