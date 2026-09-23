class Glassware:
    def __init__(self, material):
        self.material = material

class Beaker(Glassware):
    def __init__(self, material, capacity):
        Glassware.__init__(self, material)
        self.capacity = capacity

class Tray:
    def __init__(self):
        self.beakers = [Beaker("Glass", 100) for i in range(5)]

tray = Tray()

print("Tray contains 5 beakers.")
for i in range(5):
    print("Beaker", i + 1, ":", tray.beakers[i].capacity, "mL")

del tray

print("The tray is deleted, the 5 beakers is now gone")
