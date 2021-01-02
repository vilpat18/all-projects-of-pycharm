class Father:
    def __init__(self):
        super().__init__()
        print("constructor of Father class")

    def ShowF(self):
        print('father class method')

class Mother:
    def __init__(self):
        super().__init__()
        print("constructor of mother class")

    def ShowM(self):
        print('Mother class Method')


class Son(Father,Mother):

    def __init__(self):
        super().__init__()
        print('constructor of son class')

    def ShowS(self):
        print('method of son class')

s = Son()
s.ShowF()
s.ShowM()
s.ShowS()



