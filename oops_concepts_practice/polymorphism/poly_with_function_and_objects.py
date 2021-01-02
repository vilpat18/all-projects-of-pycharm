# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.status()
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)

class India():
    def capital(self):
        print("Delhi city is a capital of india")

    def language(self):
        print('hindi is widely spoke language in india')

    def status(self):
        print('india is devloping nation')

class USA():
    def capital(self):
        print('Washington DC is capital city of USA')

    def language(self):
        print("english is most widely spoken language in USA")

    def status(self):
        print("USA is a devloped nation")


def func(obj):
    obj.capital()
    obj.language()
    obj.status()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)