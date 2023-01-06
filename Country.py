class Country:
    def __init__(self, population = 40000000):
        self.population = population

class Russia(Country):
    def __init__(self, population = 146000000):
        self.population = population

class Canada(Country):
    # def __init__(self, population):
    def getPopulation(self,population):
        self.population = population

C0 = Country()
print(C0.population)

C1 = Russia()
print(C1.population)

C1 = Canada()
print(C1.population)