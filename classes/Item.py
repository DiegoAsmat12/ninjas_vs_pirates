class Item:
    def __init__(self,name,power,cantidad):
        self.name=name
        self.power = power
        self.cantidad = cantidad
    def UsarObjeto(self):
        self.cantidad-=1
