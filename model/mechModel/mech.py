import json
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

    def loadFromJson(self, j):
        self.__dict__ = json.load(j)
        for item in self.__dict__:
            if isinstance(self.__dict__[item], dict):
                part_op = part.Part()
                part_op.loadFromDict(self.__dict__[item])
                self.__dict__[item] = part_op