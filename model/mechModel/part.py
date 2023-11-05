class Part:
    def __init__(self):
        self.armor = None
        self.structure = None
        self.compartments = None
        self.components = None

    def loadFromDict(self, d):
        self. armor = d['armor']
        self. structure = d['structure']
        self. compartments = d['compartments']
        self. components = d['components']