class ElectronicDevice():
    storage = "100mb"
    memory = "20mb"
    energy_storage = 100
    energy_consumption_per_second = 10
    work = "Make a person's life easy"
    energy_source = "battery"
    fuel_type = "electricty"
    internet = False
    size = 20

    def __init__(self, name):
        self.about = (f"{name} is an Electronic Device")
        self.speed = (f"{name}'s memory consumption speed is 25mpbs ")


class PocketGadget(ElectronicDevice):
    storage = "16gb"
    memory = "1gb"
    energy_storage = 1000
    energy_consumption_per_second = 80
    size = 6

    def __init__(self, name):
        self.about = (f"{name} is a Pocket Gadget")
        self.speed = (f"{name}'s memory consumption speed is 10mpbs ")


class Phone(PocketGadget):
    storage = "64gb"
    memory = "3gb"
    energy_storage = 10000
    energy_consumption_per_second = 150
    internet = True

    def __init__(self, name):
        self.about = (f"{name} is a Phone")
        self.speed = (f"{name}'s memory consumption speed is 50mpbs ")


eniac = ElectronicDevice("ENAIC")
nokia_33_10 = PocketGadget("NOKIA THE GOD")
Redmi = Phone("REDMI")

print(eniac.storage)
print(eniac.memory)
print(eniac.internet)
print(eniac.about)
print(eniac.speed)
print()
print(nokia_33_10.storage)
print(nokia_33_10.memory)
print(nokia_33_10.about)
print(nokia_33_10.speed)
print()
print(Redmi.storage)
print(Redmi.memory)
print(Redmi.size)
print(Redmi.internet)
print(Redmi.about)
