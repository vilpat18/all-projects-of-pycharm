class India:
    def capital(self):
        print('Delhi')

class Pakistan:
    def capital(self):
        print('Islamabad')


def myfunction(obj):
    obj.capital()


I = India()
P = Pakistan()

myfunction(I)
myfunction(P)