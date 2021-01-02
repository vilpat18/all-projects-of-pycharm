class Student:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def divide(self):
        print(self.a/self.b)


obj = Student(10,5)
obj.divide()