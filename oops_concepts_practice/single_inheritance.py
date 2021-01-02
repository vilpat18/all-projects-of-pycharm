class Parent:
    def func1(self):
        print('this function is parent class')

class Child(Parent):
    def func2(self):
        print('this function is child class')

obj = Child()
obj.func2()
obj.func1()

"""  In this inheritance by creating a object of child class
     we can access both methods. it is possible beacuse the parent
     class inherite inside child class 
                                             """