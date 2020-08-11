class Pokemon:
    def __init__(self, name, type, level = 1):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 10
        self.max_health = level * 10
        self.is_knocked_out = False
        self.exp = 0
        self.max_exp = level * 10

    def __repr__(self):
        return "{name} is a {type} type Pokemon with level {level}. It has {health} hit points remaining.".format(level = self.level, name = self.name, health = self.health, type = self.type)

    def lose_health(self, points):
        self.health -= points
        if self.health <= 0:
            self.health = 0
            self.knock_out()
            print("{name} has been knocked out!".format(name = self.name))
        else: 
            print("${self.name} has lost ${points} of health!!. It now has {health} health".format(name = self.name, health = self.health))

    def gain_health(self, points):
        if self.health == 0:
            self.revive()
        self.health += points
        if self.health >= self.max_health:
            self.health = self.max_health
        print("${name} has regained ${points} of health!!".format(name = self.name))

    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print("${self.name} has been knocked out!".format(name = self.name))
    

    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 10
        print("${name} is alive again!!".format(name = self.name))

    def exp_up(self):
        self.exp += 1
        if self.exp < self.max_exp:
            print("{name} receive new exp points. Total exp points is {exp}.".format(name=self.name, exp=self.exp))
        else:
            self.exp = 0
            self.level += 1
            print("Congratulations {name} level up!!!. New level is {lvl}.".format(name=self.name, lvl=self.level))

    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print("{name} can't attack because is knocked out!".format(name = self.name))
        if self.type == 'fire' and other_pokemon.type == 'grass':
            other_pokemon.health -= self.level * 2
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif (self.type == 'grass' and other_pokemon.type == 'fire'):
            other_pokemon.health -= self.level / 2
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif(self.type == 'water' and other_pokemon.type == 'fire'):
            other_pokemon.health -= self.level * 2
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif(self.type == 'fire' and other_pokemon.type == 'water'):
            other_pokemon.health -= self.level / 2
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif(self.type == 'grass' and other_pokemon.type == 'water'):
            other_pokemon.health -= self.level
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif(self.type == 'water' and other_pokemon.type == 'grass'):
            other_pokemon.health -= self.level
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")
        elif(self.type == 'fire' and other_pokemon.type == 'grass'):
            other_pokemon.health -= self.level * 2
            print("${self.name} has attacked ${other_pokemon.name}. Its health its now at ${other_pokemon.health}")


class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)


class Trainer:
    def __init__(self, name, num_potions, pokemons):
        self.name = name
        self.potions = num_potions
        self.pokemons = pokemons
        self.current_pokemon = 0

    def __repr__(self):
        print("The trainer {name} has the following pokemon:".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon])

    def use_potion(self):
        if self.pokemons[self.current_pokemon].health == self.pokemons[self.current_pokemon].max_health:
            print("{name} has already got its maximum health!".format(name = self.pokemons[self.current_pokemon].name))
        else:
            if self.potions > 0:
                self.pokemons[self.current_pokemon].gain_health(50)
                self.potions -= 1
                print("You used a potion on {name}".format(name = self.pokemons[self.current_pokemon].name))
            else: 
                print("You don't have any potions!")

    def attack_other_trainer(self, other_trainer):
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon=other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

    def switch_active_pokemon(self, new_active):
        if new_active < len(self.pokemons) and new_active >= 0:
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make a knocked out pokemon your active pokemon.".format(name = self.pokemons[new_active].name))
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

a = Charmander(7)
b = Squirtle()
c = Squirtle(1)
d = Bulbasaur(10)
e = Charmander()
f = Squirtle(2)
    
trainer_one = Trainer("Diego", 3, [a, b, c, d])
trainer_two = Trainer("Maria", 5, [a, b, f])

print(trainer_one)
print(trainer_two)

trainer_one.attack_other_trainer(trainer_two)
trainer_two.attack_other_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.attack_other_trainer(trainer_two)
trainer_two.switch_active_pokemon(0)
trainer_two.switch_active_pokemon(1)

