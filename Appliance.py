
class EnergySupplier(object):
    """Energy_Supplier class defines the attributes and methods of an energy supplier"""

    supplier_dict = {
                     "EDF"     : {"standard": 0.17, "basic":0.16 ,"Green":0.18},
                     "PowerGen": {"standard": 0.16, "basic": 0.16,"Green":0.17}
    }

    default_supplier = "EDF"
    default_plan = "basic"
    default_tariff = supplier_dict[default_supplier][default_plan]

    def __init__(self, name = default_supplier, plan=default_plan, tariff=default_tariff):
        self.name = name
        self.plan = plan
        self.tariff = tariff

    def __str__(self):
        return ("{} is an energy supplier that charges £ {} on plan {}".format(self.name, self.tariff, self.plan))

    def get_tariff(self):
        return self.tariff

class Appliance(object):
    """The Appliance class is a base class for household appliances"""

    default_Energy_Supplier = EnergySupplier("EDF")

    def __init__(self, name="appliance", function="unknown", energy_supplier=default_Energy_Supplier):
        self.name = name
        self.function = function
        self.power_consumption = 0
        self.energy_supplier = energy_supplier

    def __str__(self):
        return "{} is an application that does the {}".format(self.name, self.function)

    def set_energy_supplier(self, energy_supplier):
        self.energy_supplier = energy_supplier

    def get_energy_supplier(self):
        return self.energy_supplier.name

    def set_power_consumption(self, power_consumption):
        self.power_consumption = power_consumption

    def calculate_cost(self, hours=0, minutes=0, seconds=0):
        rate_per_minute = self.power_consumption / 60
        rate_per_second = self.power_consumption / 60
        total_kw = self.power_consumption * hours + minutes * rate_per_minute + seconds * rate_per_second
        total_cost_pence = total_kw * self.energy_supplier.tariff
        total_cost_pounds = round(total_cost_pence / 100, 2)
        return_string = f"Your {self.name} rated a {self.power_consumption} kwh costs a total of £ {total_cost_pounds} to run for {hours} hours, {minutes} minutes and {seconds} seconds"
        return return_string


class Toaster(Appliance):
    """Toaster Class is a subclass of Appliance and defines the attributes and methods of a toaster"""
    default_power_consumption = 150

    def __init__(self, slots=2):
        super().__init__()
        self.name = "Toaster"
        self.function = "Toasts Slices of Bread"
        self.slots = slots
        self.set_power_consumption(Toaster.default_power_consumption)


class Vacuum(Appliance):
    """ Vacuum class is a subclass of Appliance and defines the attributes and methods of a vacuum cleaner"""
    default_power_consumption = 350

    def __init__(self):
        super().__init__()
        self.name = "Vacuum Cleaner"
        self.function = "Vacuums The Floor"
        self.set_power_consumption(Vacuum.default_power_consumption)


class Fridge(Appliance):
    """ Fridge class is a subclass of Appliance and defines the Attributes and methods of a refrigerator"""
    default_power_consumption = 275

    def __init__(self, fridge_type="under_counter"):
        super().__init__()
        self.name = "Refrigerator"
        self.function = "Keeps food items cool"
        self.fridge_type = fridge_type
        self.set_power_consumption(Fridge.default_power_consumption)

