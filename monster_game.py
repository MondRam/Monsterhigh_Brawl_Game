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
