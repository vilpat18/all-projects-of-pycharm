class Mother:
    mother_name = ' '
    def mother(self):
        print(self.mother_name)

class Father:
    father_name = ''
    def father(self):
        print(self.father_name)

class son(Mother,Father):
    def parent(self):
        print(self.father_name)
        print(self.mother_name)

obj = son()
obj.mother_name = 'twinkle'
obj.father_name = 'akshay'
obj.father()
obj.mother()
print('-------------------------------')
obj.parent()



