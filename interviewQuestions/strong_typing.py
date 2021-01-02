class india:
    def language(self):
        print('hindi')

class usa:
    def language(self):
        print('english')


class srilanka:
    def capital(self):
        print('colombo')


def myfunction(obj):
    if hasattr(obj,'language'):
        obj.language()
    elif hasattr(obj,'capital'):
        obj.capital()


i = india()
u = usa()
s = srilanka()

myfunction(i)
myfunction(u)
myfunction(s)