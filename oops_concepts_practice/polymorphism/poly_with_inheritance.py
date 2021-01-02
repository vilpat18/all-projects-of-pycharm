class Bird:
    def intro(self):
        print('there are many types of birds ')

    def flight(self):
        print('some of birds can fly but sum cannot')

class sparrow(Bird):
    def flight(self):
        print('sparrow can fly')

class ostrich(Bird):
    def flight(self):
        print('ostrich cannot fly')

obj_bird = Bird()
obj_sparrow = sparrow()
obj_ostri = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_sparrow.intro()
obj_sparrow.flight()

obj_ostri.intro()
obj_ostri.flight()