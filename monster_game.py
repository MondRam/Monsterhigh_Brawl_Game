#Monsterhigh_Brawl_Game
''' MONSTERHIGH BRAWL GAME 
Montserrat Guadalupe Ramírez Esparza
Sofia Abilene Campos Hernandez'''

#Import the random library to choose random elements
import random

#Create a class to represent a type of monster
class MonsterhighType:
    def __init__(self, name, strengths=None, weaknesses=None):
        self.name = name
        self.strengths = [] if strengths is None else strengths
        self.weaknesses = [] if weaknesses is None else weaknesses
 #Check what type of monster it is strong against        
    def strong_against (self, other):
        return other.name in self.weaknesses
        
#Check what type of monster it is weak against        
    def is_weak_against(self, other):
        return other.name in self.strengths
    
#Represents a Monster with name, level, types and adds two types of attacks
class Monsterhigh:
    
    def __init__(self, name, level, types):
        self.name = name
        self.level = level
        self.types = types
        self.max_health = level * 10
        self.current_health = self.max_health
        self.is_ko = False
        self.general_attack = "None"
        self.special_attack = "None"

#Returns the characteristics of the Monster    
    def __repr__(self):
        type_names = "/".join([t.name for t in self.types])
        return f"{self.name} ({type_names} - Level {self.level})"

#Decreases the Monster´s health by specific damage
    def lose_health(self, damage):
        self.current_health = max(0, self.current_health - damage)
        if self.current_health == 0:
            self.ko()

#Increases the Monster´s health by the specific health amount
    def gain_health(self, heal):
        self.current_health = min(self.max_health, self.current_health + heal)

#Indicates that a Monster was knocked out
    def ko(self):
        self.is_ko = True

#Revives the Monster
    def revive(self):
        self.is_ko = False
        self.current_health = self.max_health

#Calculate the effectiveness of the Monster against other types of Monsters, take into account the weaknesses and strengths
    def get_effectiveness(self, other_type):
        effectiveness = 1.0
        for type in self.types:
            for strength in type.strengths:
                if strength == other_type.name:
                    effectiveness *= 2.0
            for weakness in type.weaknesses:
                if weakness == other_type.name:
                    effectiveness *= 0.5
        return effectiveness

#Attack another Monster and reduce its health based on the effectiveness, this is a simple attack    
    def attack(self, other):
        effectiveness = self.get_effectiveness(other.types[0])
        if len(other.types) > 1:
            effectiveness *= self.get_effectiveness(other.types[1])
        damage = int(((2 * self.level / 5 + 2) * 40 *
                      self.level / other.level / 50 + 2) * effectiveness)
        print(f"{self} attacks {other} with {self.general_attack} and deals {damage} damage!")
        other.lose_health(damage)

#Attack another Monster and reduce its health based on the effectiveness, this is a special attack        
    def attack_two(self, other):
        effectiveness = self.get_effectiveness(other.types[0])
        if len(other.types) > 1:
            effectiveness *= self.get_effectiveness(other.types[1])
        damage = int(((2 * self.level / 5 + 3) * 40 *
                      self.level / other.level / 50 + 2) * effectiveness)
        print(f"{self} attacks {other} with {self.special_attack} and deals {damage} damage!")
        other.lose_health(damage)

#simulates a battle between two Monsters using only simple attacks
def battle(monster1, monster2):
    print(" ")
    print(f"~~~~ {monster1} vs. {monster2}! Let the monstrous battle begin! ~~~~")
    current_turn = 1
    while not monster1.is_ko and not monster2.is_ko:
        print(" ")
        print(f"Round {current_turn}!")
        attacker = monster1 if current_turn % 2 == 1 else monster2
        defender = monster2 if current_turn % 2 == 1 else monster1
        attacker.attack(defender)
        current_turn += 1
    winner = monster1 if  monster2.is_ko else monster2
    print(" ")
    print(f"~~~~ {winner} wins! ~~~~")
    fighters = monster1 and monster2
    fighters.revive()
    fighters.gain_health(100)
   
#Simulates a battle between two Monsters, one selected by the user and another randomly selected
#They will fight round by round 
def battle_two(monster1, monster2):
    print(" ")
    print(f"~~~~ {monster1} vs. {monster2}! Let the monstrous battle begin! ~~~~~")
    current_turn = 1
    while not monster1.is_ko and not monster2.is_ko:
        print(" ")
        print(f"Round {current_turn}!")
        attacker = monster1 if current_turn % 2 == 1 else monster2
        defender = monster2 if current_turn % 2 == 1 else monster1
        if current_turn % 2 ==0:
            attacker.attack(defender)
            current_turn += 1
        else:
            print(f"{monster1} choose your attack: simple attack(1) or special attack(2) ")
            option = input()
            if option == "1":
                attacker.attack(defender)
            elif option == "2":
                attacker.attack_two(defender)
            current_turn += 1
    winner = monster1 if  monster2.is_ko else monster2
    print(" ")
    print(f"~~~~ {winner} wins! ~~~~")
    fighters = monster1 and monster2
    fighters.revive()
    fighters.gain_health(100)
 
#Simulates a battle between two Monsters using simple attacks and special attacks
#Allows users to play round by round and select the attack they want to use
def battle_three(monster1, monster2):
    print(" ")
    print(f"~~~~ {monster1} vs. {monster2}! Let the monstrous battle begin! ~~~~")
    current_turn = 1
    while not monster1.is_ko and not monster2.is_ko:
        print(" ")
        print(f"Round {current_turn}!")
        attacker = monster1 if current_turn % 2 == 1 else monster2
        defender = monster2 if current_turn % 2 == 1 else monster1
        if current_turn % 2 ==0:
            print(f"{monster2} choose your attack: simple attack(1) or special attack(2) ")
        else:
            print(f"{monster1} choose your attack: simple attack(1) or special attack(2) ")
        option = input()
        if option == "1":
            attacker.attack(defender)
        elif option == "2":
            attacker.attack_two(defender)
        current_turn += 1
    winner = monster1 if  monster2.is_ko else monster2
    print (" ")
    print(f"~~~~ {winner} wins! ~~~~")
    fighters = monster1 and monster2
    fighters.revive()
    fighters.gain_health(100)
    
#Define the Monster types  
vampire_type = MonsterhighType("Vampire", strengths=["Zombie"], weaknesses=["Mummy"])
frankenstein_type = MonsterhighType("Frankenstein", strengths=[], weaknesses=[])
mummy_type = MonsterhighType("Mummy", strengths=["Vampire"], weaknesses=["Zombie"])
zombie_type = MonsterhighType("Zombie", strengths=[], weaknesses=[])
sea_monster_type = MonsterhighType("Sea Monster", strengths=[], weaknesses=[])
werewolf_type = MonsterhighType("Werewolf", strengths=[], weaknesses=[])
ghost_type = MonsterhighType("Ghost", strengths=[], weaknesses=[])
