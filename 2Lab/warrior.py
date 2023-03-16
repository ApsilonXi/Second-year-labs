class warrior:

    def __init__(self, warrior):
        self.warrior = warrior
        self.Warriorweapon = 'Меч'

    def virtualMethod(self):
        raise NotImplementedError
    def usesvirtualMethod(self):
        return self.virtualMethod()
W = warrior(warrior='')
    
