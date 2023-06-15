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
