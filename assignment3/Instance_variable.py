class Math:
    def __init__(self,a,b):
        self.a= a
        self.b= b
    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def first(self):
        self.a=100
        self.b=200


obj = Math(30,20)
obj.first()
print(obj.add())
print(obj.sub())
print(obj.mul())






