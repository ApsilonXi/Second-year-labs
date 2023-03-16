class matros:

    def __init__(self, matros):
        self.matros = matros
        self.Matrosweapon = 'Кортик'

    def virtualMethod(self):
        raise NotImplementedError()
    def usesvirtualMethod(self):
        return self.virtualMethod()
M = matros(matros='')