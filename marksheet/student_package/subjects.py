class Subjects:
    def __init__(self):
        self.math = int(input("math: "))
        self.physics = int(input("physics: "))
        self.chem = int(input("chem: "))

    def __str__(self):
        return 'math: {}| physics: {}| chem: {}'.format(self.math,self.physics,self.chem)

    @property
    def get_math(self):
        return self.math

    @property
    def get_physics(self):
        return self.physics

    @property
    def get_chem(self):
        return self.chem

    @get_math.setter
    def get_math(self,value):
        self.math = value

    @get_physics.setter
    def get_physics(self,value1):
        self.physics = value1

    @get_chem.setter
    def get_chem(self,value2):
        self.chem = value2

if __name__=="__main__":
    obj2 = Subjects()
    print(obj2)


