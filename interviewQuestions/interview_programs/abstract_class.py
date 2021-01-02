from abc import ABC,abstractmethod

class India(ABC):
    @abstractmethod
    def capital(self):
        pass

class Maha(India):
    def capital(self):
        print('mumbai is capital of maha')

class Andhra(India):
    def capital(self):
        print('amaravti is capital of andhra')


mh = Maha()
ap = Andhra()
mh.capital()
ap.capital()

