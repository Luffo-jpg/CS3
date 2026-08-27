# RPG Hero Game
class Hero:
    def __init__(self,name,HP):
        self.name = name
        self.HP = HP
    def take_damage(self, amount):
        self.HP = self.HP - amount
Arthur = Hero("Arthur", 100)
Morgana = Hero("Morgana", 100)
Arthur.take_damage(10)
print("Arthur's HP =", Arthur.HP)
print("Morgana's HP =", Morgana.HP)

