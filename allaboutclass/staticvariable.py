class student:
    x = 1000; y = 20; z = 30
    def __init__(self):
        self.a = "vilas"
    @classmethod
    def name(cls):
        cls.x = 78
        cls.y = 999
obj = student()
print(obj.a)
obj1 = student()
obj1.name()
print(student.__dict__)
obj.x = obj.x + 100
obj.y = obj.y + 200
obj.z = obj.z + 300
print("obj:", obj.x, obj.y, obj.z)
print(student.x, student.y, student.z)


