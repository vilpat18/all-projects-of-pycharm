class Grandfather:
    grandfather_name = 'harivanshrai'

    def grandfather(self):
        print(self.grandfather_name)

class Father(Grandfather):
    father_name = 'amitabh'

    def father(self):
        print(self.father_name)

class Child(Father):
    child_name = 'abhishek'

    def legacy(self):
        print(self.grandfather_name)
        print(self.father_name)
        print(self.child_name)


obj = Child()
obj.legacy()
