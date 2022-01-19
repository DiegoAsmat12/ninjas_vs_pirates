from Pirate import Pirate
class ArmedPirate(Pirate):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 20
        self.speed = 1
        self.health = 200

