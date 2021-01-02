class Robot:
    def __init__(self):
        self.a = 123
        self._b = 456
        self.__c = 789

obj = Robot()
print(obj.a)
print(obj._b)
# print(obj.__c)

# output :--- attribute erroe robot object has no attributr __c


class Robot_make:
    def __init__(self):
        self.__version = 22

    def getversion(self):
        print(self.__version)

    # def setversion(self,version):
    #     self.__version = version

obj = Robot_make()
obj.getversion()
# obj.setversion('2.5')
obj.getversion()