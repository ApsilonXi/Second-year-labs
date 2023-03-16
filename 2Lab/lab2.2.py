class newClass:
    def __init__(self):
        self.KEEP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def Keep(self):
        for i in range(len(self.KEEP)):
            for j in range(len(self.KEEP)):
                self.KEEP[i][j] = int(input('Введите число: '))

    def __add__(self, num):
        for i in range(len(self.KEEP)):
            for j in range(len(self.KEEP)):
                    self.KEEP[i][j] += num
            print(self.KEEP[i])

Class = newClass()
Class.Keep()
Class.__add__(5)
Class + 5

