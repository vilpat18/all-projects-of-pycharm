class Student:
    University = 'PuneUniversity'

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def student_info(self):
        print(self.first_name, self.last_name)

    @classmethod
    def info(cls):
        return cls.University


obj = Student('vilas','patil')
obj.student_info()

print(Student.info())
