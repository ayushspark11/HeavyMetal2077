from collections import namedtuple
from . import part

class Mech:
#TODO: refactor as named tuple
    class Component:
        name = None
        type = None
        size = None
        isDestroyed = False
        range = None
        heat = None
        damage = None
        ammo = None
        pilotingModifier = None
        movementModifier = None
        gunneryModifier = None
        forceTest = None
        #TODO: determine where modifiers affect
        effectDistance = None

    #class Part:
    #    def __init__(self):
    #        self.armor = None
    #        self.structure = None
    #        self.compartments = None
    #        self.components = None

        #def __dict__(self):
        #    return self.__dict__

    def __init__(self):
        self.head = part.Part()
        self.centerTorso = part.Part()
        self.leftTorso = part.Part()
        self.rightTorso = part.Part()
        self.leftArm = part.Part()
        self.rightArm = part.Part()
        self.leftLeg = part.Part()
        self.rightLeg = part.Part()
        #walk = None
        #run = None
        #jump = None
        #tonnage = None
        #cost = None
        #battleValue = None

    def asDict(self):
        dict_op = self.__dict__
        #print(dict_op)

        for item in dict_op:
            #print(item)
            dict_op[item] = dict_op[item].__dict__
        #dict["children"] = [child.__dict__ for child in dict["children"]]
        #print(dict_op)
        return dict_op