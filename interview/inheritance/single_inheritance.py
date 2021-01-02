class parent:
    def func1(self):
        print('this is in parent class')

class child(parent):
    def func2(self):
        print('this is in child class')

obj = child()

obj.func1()
obj.func2()