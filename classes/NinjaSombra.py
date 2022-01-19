from Ninja import Ninja
from ControlInventario import ControlInventario
class NinjaSombra(Ninja):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 50
        self.inmune = False
        ControlInventario.AñadeOSobreescribe(NinjaSombra.inventario,"Bomba de Humo", 0, 5)
    
    def bombaDeHumo(self):
        self.inmune=True
        ControlInventario.usaItem(NinjaSombra.inventario,"Bomba de Humo")


