class Person:
    species = 'human'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"the age of {self.name}  is {self.age} years old"

    def profession(self,field):
        return f"{self.name} the proffetion in {field}"

a = Person('ajay',45)
b = Person('mahesh',58)

print(a)
print(b)
