class Animal:
    legs = 4
    @staticmethod
    def dog():
        print("the dog walk with {} legs ".format(Animal.legs))
    @staticmethod
    def variable():
        Animal.cat=4
        print("the cat has {} legs".format(Animal.cat))



obj = Animal()
obj.dog()
obj.variable()
