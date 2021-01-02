class Person(object):
    def __init__(self,name):
        self.name = name

    def Get_name(self):
        return self.name

    def is_employee(self):
        return False

class Employee(Person):

    def is_employee(self):
        return True


emp = Person('vilas')
print(emp.Get_name(),emp.is_employee())

emp = Employee('vilasp')
print(emp.Get_name(),emp.is_employee())

# her we inherite class person inside the class employee so that we access the all methods
# of class person assinging same object