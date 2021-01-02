# Instance methods are functions that are defined inside a class and only be a called from
# Instance of that class

class Car:
    species = 'Race car'

    def __init__(self,name,year):
        self.name = name
        self.year = year

    def description(self):
        return f"{self.name} is {self.year} model"

    def price(self,high):
        return f"{self.name}  price is {high} which is very high"

road_race = Car('ferrari',2015)
hill_race = Car('jaguar',2019)

print(road_race.description())
print(hill_race.description())

print(road_race.species)


print(road_race.price('25000000'))
print(hill_race.price(80))