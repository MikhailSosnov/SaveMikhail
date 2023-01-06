class Games:
    year = 1984
    def getName(self, Name = 'Ralf'):
        self.Name = Name
        return(self.Name)

class PCGames(Games):
    def getName(self, Name = 'Solomon'):
        self.Name = Name
        return(self.Name)

class PC4Games(Games):
    def getName(self, Name = 'Tolun'):
        self.Name = Name
        return(self.Name)

class XboxGames(PC4Games):
    def getName(self, Name='Urban'):
        self.Name = Name
        return (self.Name)

class MobileGames(Games):
    def getName(self, Name='Fedora'):
        self.Name = Name
        return (self.Name)

Games.year = 2111

print(Games().year)
print(Games().getName())

print(PCGames.year+2)
print(Games().getName('Olaf'))

PC4Games.year = 1937
print(Games().year)
print(PC4Games.year+2)

print(XboxGames.year+2)




# g1 = Games()
# print (g1.getName('Asmar'))
# print(Games().getName())
#
# print(Games().year)
#
# Games.year = '2000'
# print(Games.year)




