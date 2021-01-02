class Parent:
    def func1(self):
        print('this is in parent class')

class child1(Parent):
    def func2(self):
        print("this is in child1 class")

class Child2(Parent):
    def func3(self):
        print("this is in child2 class")


obj1 = child1()

obj1.func1()
obj1.func2()

obj2 = Child2()

obj2.func1()
obj2.func3()

