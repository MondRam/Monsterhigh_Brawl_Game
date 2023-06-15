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
 