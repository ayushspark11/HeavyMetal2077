from collections import namedtuple
from . import part

class Mech:
#TODO: consider refactor as named tuple
    def __init__(self):
        self.head = part.Part()
        self.centerTorso = part.Part()
        self.leftTorso = part.Part()
        self.rightTorso = part.Part()
        self.leftArm = part.Part()
        self.rightArm = part.Part()
        self.leftLeg = part.Part()
        self.rightLeg = part.Part()
        self.walk = None
        self.run = None
        self.jump = None
        self.tonnage = None
        self.cost = None
        self.battleValue = None