class Component:
    def __init__(self):
        self.name = None
        self.type = None
        self.size = None
        self.isDestroyed = False
        self.range = None
        self.heat = None
        self.damage = None
        self.ammo = None
        self.pilotingModifier = None
        self.movementModifier = None
        self.gunneryModifier = None
        self.forceTest = None
        #TODO: determine where modifiers affect
        self.effectDistance = None