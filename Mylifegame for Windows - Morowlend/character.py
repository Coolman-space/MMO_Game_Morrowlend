import random


class Character:
    def __init__(self, name, health, mana, attack, defense, magic, items):
        self.name = name
        self.health = health
        self.health_max = 100
        self.mana = mana
        self.mana_max = 100
        self.attack_low = attack - 5
        self.attack_high = attack + 5
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic','Lose']

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health

    def heal(self, damage):
        self.health += damage
        if self.health > self.health_max:
            self.health = self.health_max

    def reduce_mana(self, cost):
        self.mana -= cost

    def rand_spell(self):
        spell = random.randrange(0, len(self.magic))
        return spell



    def display_actions(self):
        print("\n")
        print("╔═══════════════════════════╗")
        print("║          Actions          ║")
        print("╚═══════════════════════════╝")
        print("What would you like to do?\n")
        i = 1
        for j in self.actions:
            print(str(i) + ". " + j)
            i += 1

    def display_spells(self):
        print("\n")
        print("╔══════════════════════════╗")
        print("║          Spells          ║")
        print("╚══════════════════════════╝")
        i = 1
        for j in self.magic:
            print(str(i) + ". " + j.name)
            i += 1

    def display_items(self):
        print("\n")
        print("╔═════════════════════════╗")
        print("║          Items          ║")
        print("╚═════════════════════════╝")
        i = 1
        for j in self.items:
            print(str(i) + ". " + j.name + " - " + j.description + " (" + str(j.amount) + "x)")
            i += 1
