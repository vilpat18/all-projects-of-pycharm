class Test:
    a = 11; z = 888
    def __init__(self):
        Test.b = 100
        self.c = 200
        self.m = 400

    @classmethod
    def math(cls):
        cls.n = 1000
        #         #del cls.b delete by classmethod by using cls
        pass
obj = Test()
obj.math()
print(obj.__dict__)
print(Test.a, Test.b, Test.z,Test.n)  # access by class name
print(obj.b, obj.a, obj.n, obj.z)  # access by reference variable

