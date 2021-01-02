class mother:
    mother_name = 'jaya bacchan'

    def mother(self):
        print(self.mother_name)


class father:
    father_name = 'amitabh bacchan'

    def father(self):
        print(self.father_name)


class son(mother, father):
    def parent(self):
        print(self.mother_name)
        print(self.father_name)


obj = son()
obj.parent()
