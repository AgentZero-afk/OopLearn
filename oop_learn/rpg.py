class Character:
    def __init__(self,name,damage):
        self._health = 100
        self._name = name
        self._damage = damage

    def get_status(self):
        return f'Имя: {self._name}, Здоровье: {self._health}'

    def take_damage(self,amount):
        self._health -= amount

    def attack(self,target):
        target.take_damage(self._damage)


class Warrior(Character):
    def __init__(self,name,damage,armor):
        super().__init__(name,damage)
        self.armor = armor

    def take_damage(self,ammount):
        ammount -= self.armor
        super().take_damage(ammount)

class Mage(Character):
    def __init__(self,name,damage,mana):
        super().__init__(name,damage)
        self.mana = mana

    def attack(self,target):
        mana_cost = 10
        if self.mana >= mana_cost:
            super().attack(target)
            self.mana -= mana_cost

warrior = Warrior("Конан", 15, 5)
mage = Mage("Раистлин", 20, 100)

print(warrior.get_status())
print(mage.get_status())
print("--- Битва ---")


mage.attack(warrior)
print(warrior.get_status())


warrior.attack(mage)
print(mage.get_status())

mage.mana = 5
mage.attack(warrior)
print(warrior.get_status())