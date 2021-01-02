from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print('concnrete method')


class Child(Father):
    def disp(self):
        a= 10
        b = 20
        print(a+b)
        print('child class')


abs = Child()
abs.disp()
abs.show()