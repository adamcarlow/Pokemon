#Pokemon Terminal game for Code Academy CS101 Final Project
import random
class Pokemon():

  def __init__(self, type, attack, defense, weakness, name):
    self.type = type
    self.attack = attack
    self.defense = defense
    self.weakness = weakness
    self.name = name

    
  def battle(player1, player2):
    while player2.defense > 0: 
      player1_attack = round((player1.attack * random.random()),0)
      player2.defense = player2.defense - player1_attack
      if player2.defense > 0:
        print("{p} does ".format(p=player1.name) + str(player1_attack) + ' damage to {p2}!'.format(p2=player2.name))
        print('{p2} has {d2} life left!'.format(p2=player2.name,d2=player2.defense))
      else:
        print("{p} does ".format(p=player1.name) + str(player1_attack) + ' damage to {p2}!'.format(p2=player2.name))
        print('{p2} has been defeated!'.format(p2=player2.name,d2=player2.defense))
    

#print("Creating circle with diameter {d}".format(d=diameter)) 
Charizard = Pokemon('Fire',120,275,'Water','Charizard')
Snorlax = Pokemon("Colorless",90,350,'Fighting','Snorlax')

characters = [Charizard, Snorlax]
#input1 = input("Which character will you choose player1? ")
#input2 = input("Which character will you choose player2? ")
player1 = random.choice(characters)
player2 = random.choice(characters)
print('Player1 you will be ' + player1.name)
print('Player2 you will be ' + player2.name)
#print(Charizard.type)
#print(Charizard.attack)
#print(Charizard.defense)
#print(Charizard.weakness)
#print(Snorlax.weakness)
battle1 = Pokemon.battle(player1,player2)
battle2 = Pokemon.battle(player1,player2)
battle3 = Pokemon.battle(player1,player2)
battle4 = Pokemon.battle(player1,player2)
battle5 = Pokemon.battle(player1,player2)
battle6 = Pokemon.battle(player1,player2)
#print(Snorlax.type)
#print(Snorlax.attack)
#print(Snorlax.defense)
#print(Snorlax.weakness)
