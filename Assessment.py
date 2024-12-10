import random

##Entities
class entity():
    def __init__(self, ac, hp):
        self.ac = ac
        self.MaxHp = hp
        self.hp = hp
        
    def checkDistance(self, target):
        distance = 0
        #To be expanded upon
        return distance
    def act():
        pass
        pass
#Players
class player(entity):
    def __init__(self, race, ac, hp = 100):
        super().__init__(ac, hp)
        self.race = race
        self.inventory = []
        pass
    

class fighter(player):
    def __init__(self, race, ac, hp, weapon):
        super().__init__(race, ac, hp)
        self.weapon = weapon
    pass

class wizard(player):
    def __init__(self, race, ac, hp, spell):
        super().__init__(race, ac, hp)
        self.spell = spell
    pass

#Monsters
class monster(entity):
    def __init__(self, ac, hp):
        super().__init__(ac, hp)
        pass

class wolf(monster):
    def __init__(self, ac, hp):
        super().__init__(ac, hp)
    pass

class goblin(monster):
    def __init__(self, ac, hp):
        super().__init__(ac, hp)
    pass

class goblinWizard(goblin):
    def __init__(self, ac, hp):
        super().__init__(ac, hp)
    
    pass

class goblinFighter(goblin):
    pass


##Attacks
class attack():
    def __init__(self, range, damage, dmgType):
        self.range = range
        self.damage = damage
        self.dmgType = dmgType
        pass
    
    def act(self):
        print("Attacking...")
        pass
        
class spell(attack):
    def __init__(self, range, damage, aoe=1):
        super().__init__(range, damage)
        self.hasAoE = aoe
        
    def act(self, player):
        target = input("Choose Target: ")
        if player.distance(target) < self.range:
            if self.hasAoE > 1:
                dmg = random.randint(1, self.damage)
                for entity in AllEntites:
                    if entity.distance(target) > self.hasAoE:
                        entity.hp = entity.hp - dmg
            else random.randint(1,20) > target.ac:
                target.hp = target.hp - random.randint(1,self.damage)
    pass

class weapon(attack):
    def __init__(self, range, damage, loading=False):
        super().__init__(range, damage)
        self.isLoading = loading
    
    def act(self, player):
        target = input("Choose Target: ")
        if player.distance(target) < self.range:
            if random.randint(1,20) > target.ac:
                target.hp = target.hp - random.randint(1,self.damage)
    pass



##Objects - furniture, consumable items
class objects():
    def __init__(self, size):
        self.size = size
        pass
    def use(self):
        print("Using...")
        pass
    pass

class chest(objects):
    def __init__(self, size, storage=1, items = []):
        super().__init__(size)
        self.storage = [' ' for i in range(storage)]
        for i in range(len(items)):
            if self.storage[i] == ' ' and i<len(items):
                self.storage[i] = items[i]
    def use(self, player):
        space = 'Nowhere'
        spot = 0
        print("Items in chest:")
        print (self.storage)
        action = input("What do you want to do? ")
        if action == "Add":
            while space != ' ':
                space = self.storage[spot]
                spot = spot+1
            add = input("what to add? ")
            if add in player.inventory:
                self.storage.add(add)
                player.inventor.remove(add)
            
        if action == "Take":
            take = input("What would you like to take? ")
            if take in self.storage:
                player.inventor.append(take)
                self.storage.remove(take)
                pass
    pass

class healthPotion(objects):
    def __init__(self, size):
        super().__init__(size)
        
    def use(self, player):
        print("Drinking Health Potion")
        heal = random.randint(1,100)
        player.hp = player.hp + heal
        print("Healed", heal, "hp")
        if player.hp > player.MaxHp:
            player.hp = player.MaxHp
            print("Max Hp")
        pass
    pass

##Game
class DnD():
    def __init__(self, players = []):
        self.party = players
        pass
    def round(self):
        pass
