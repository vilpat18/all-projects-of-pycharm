class Grandfather:
    grand_father_name = 'dattatray'
    def grandfather(self):
        print(self.grand_father_name)

class Father(Grandfather):
    father_name = 'baswaraj'
    def father(self):
        print(self.father_name)

class son(Father):
    def parent(self):
        print(self.grand_father_name)
        print(self.father_name)

obj = son()
# obj.grand_father_name = 'dattatray'
# obj.father_name = 'baswaraj'
obj.parent()