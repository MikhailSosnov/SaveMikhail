class MightestWeapon:
    name = 'Empaer'
    def __init__(self, weapon_type):
        self.wrapon_type = weapon_type

print(MightestWeapon.name)

MightestWeapon.name = 'Steel Sword'

hero_sword = MightestWeapon('sword')

hero_sword.name = 'Excalibur'

print(hero_sword.name)
print(MightestWeapon.name)