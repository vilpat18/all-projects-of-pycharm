class parent:
    def __init__(self):
        self.value = 'inside parent'
    def show(self):
        return self.value

class child(parent):
    def __init__(self):
        self.value = 'inside child'
    def show(self):
        return self.value

obj1 = parent()
obj2 = child()

print(obj1.show())
print(obj2.show())
