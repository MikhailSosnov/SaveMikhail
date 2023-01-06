class Games:
    def __init__(self, year = 1970):
        self.year = year

    def getName(self, Name = 'Ralf'):
        self.Name = Name
        return(self.Name)

class PCGames(Games):
    def getName(self, Name = 'Solomon'):
        self.Name = Name
        return(self.Name)

class PC4Gemes(Games):
    def getName(self, Name = 'Tolun'):
        self.Name = Name
        return(self.Name)

class XboxGames(Games):
    def getName(self, Name='Urban'):
        self.Name = Name
        return (self.Name)

class MobileGames(Games):
    def getName(self, Name='Fedora'):
        self.Name = Name
        return (self.Name)

Games.year = 2111

print(Games().getName())

print(PCGames.year)
print(Games().getName('Olaf'))
print(Games().year)


Games.year = 3111

print(Games(3000).year)

print(Games().year)

# g1 = Games()
# print (g1.getName('Asmar'))
# print(Games().getName())
#
# print(Games().year)
#
# Games.year = '2000'
# print(Games.year)




