# Class is a blueprint for how something should defined
# Classes defines functions called methods
# Classes are used to create user defined data structure

class Dog:
    # Class Attribute
    species = 'canies familieres'

    # Constructer method

    def __init__(self,name,age):
        self.name = name
        self.age = age

# following labra and pashmi are instances

labra = Dog('tommy',10)
pashmi = Dog('rocky',9)

print(labra.name,labra.age)
print(pashmi.age,pashmi.name)

print(labra.species)
print(pashmi.species)

pashmi.species = 'tiger family'
labra.species = 'donkey family'

print(labra.species)
print(pashmi.species)
