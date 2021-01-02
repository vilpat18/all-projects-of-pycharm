class child:
    # constructor
    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def is_student(self):
        return False

class Student(child):

    def is_student(self):
        return True

a = child('aarav')
print(a.get_name(),a.is_student())

a = Student('ajay')
print(a.get_name(),a.is_student())
