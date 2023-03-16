class pehot:

    def __init__(self, pehotinets):
        self.pehotinets = pehotinets
        self.Pehotweapon = 'Винтовка'

    def virtualMethod(self):
        raise NotImplementedError()
    def usesvirtualMethod(self):
        return self.virtualMethod()
P = pehot(pehotinets='')
        