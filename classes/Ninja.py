from Item import Item
class Ninja:

    inventario = []

    def __init__( self , name="" ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self

    @classmethod
    def addToInventory(cls,name,power,cantidad):
        itemItem = Item(name,power,cantidad)
        cls.inventario.append(itemItem)
