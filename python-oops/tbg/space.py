class SpaceShip:
    def __init__(self, name, health, inventory, fuel_level = 0):
        self.name = name
        self.fuel_level = fuel_level
        self.health = health
        self.inventory = inventory

    def changeInFuel(self, level, flag):
        if flag == 'a' and self.fuel_level == 100 :
            print("Tank already FULL")
            return 1
        elif flag == 'd' and self.fuel_level == 0 :
            print("!Tank EMPTY!")
            return 1
        if flag == 'a' :
            if 100 - self.fuel_level < level :
                self.fuel_level = 100
            else :
                self.fuel_level += level
            return 1
        if flag == 'd' :
            if self.fuel_level - level < 0 :
                print("Fuel Not Sufficient")
                return -1
            else :
                self.fuel_level -= level
                if self.fuel_level < 20 :
                    print('LOW FUEL')
                return

def main():
    ship = SpaceShip("Yuki", "100", "100", ["apple"])
