class India():
    def language(self):
        print('in india hindi is commonly know language')

    def Capital(self):
        print('delhi is a capital of india')

    def status(self):
        print('india is a devloping nation')

class USA():
    def language(self):
        print('in USA english is commonly known language')

    def Capital(self):
        print('california is a capital of USA')

    def status(self):
        print('USA is devloped country')

obj1 = India()
obj2 = USA()

for i in (obj1,obj2):
    i.language()
    i.Capital()
    i.status()