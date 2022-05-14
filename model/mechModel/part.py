class Part:
        def __init__(self):
            self.armor = None
            self.structure = None
            self.compartments = None
            self.components = None

        def asDict():
            return self.__dict__