class School:
    def func1(self):
        print('this function is school')

class Student1(School):
    def func2(self):
        print('this function is student 1')

class student2(School):
    def func3(self):
        print('this function is student 2')

class student3(Student1,student2,School):
    def funct4(self):
        print('this functon is student 3')

obj = student3()
obj.func1()
obj.func2()
obj.func3()
obj.funct4()