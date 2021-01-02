class Parent:
    def func1(self):
        print('this function is base class')

class Child1(Parent):
    def func2(self):
        print('this function is child class 1')

class Child2(Parent):
    def func3(self):
        print('this function is child class 2')


obj = Child1()
obj1 = Child2()
obj.func1()
obj.func2()
obj1.func1()
obj1.func3()