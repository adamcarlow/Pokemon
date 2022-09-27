#Pokemon Terminal game for Code Academy CS101 Final Project
import random
class Pokemon():

  def __init__(self, type, attack, defense, weakness, name):
    self.type = type
    self.attack = attack
    self.defense = defense
    self.weakness = weakness
    self.name = name

    
  def battle(first, second):
    while first.defense > 0 and player2.defense > 0:
      first_attack = round((first.attack * random.random()),0)
      second.defense = second.defense - first_attack
      second_attack = round((second.attack * random.random()),0)
      first.defense = first.defense - second_attack
      if second.defense > 0:
        print("{p} does ".format(p=player1.name) + str(first_attack) + ' damage to {p2}!'.format(p2=second.name))
        print('{p2} has {d2} life left!'.format(p2=second.name,d2=second.defense))
      else:
        print("{p} does ".format(p=player1.name) + str(first_attack) + ' damage to {p2}!'.format(p2=second.name))
        print('{p2} has been defeated!'.format(p2=second.name,d2=second.defense))
    #while player1.defense > 0: 
      print('')
      if first.defense > 0:
        print("{p} does ".format(p=second.name) + str(second_attack) + ' damage to {p1}!'.format(p1=first.name))
        print('{p1} has {d1} life left!'.format(p1=first.name,d1=first.defense))
      else:
        print("{p} does ".format(p=second.name) + str(second_attack) + ' damage to {p1}!'.format(p1=first.name))
        print('{p1} has been defeated!'.format(p1=first.name,d1=first.defense))
      print('')
    

#print("Creating circle with diameter {d}".format(d=diameter)) 
Charizard = Pokemon('Fire',90,275,'Water','Charizard')
Snorlax = Pokemon("Colorless",45,350,'Fighting','Snorlax')
Mew = Pokemon("Psychic",75,240,'Darkness','Mew')

characters = [Charizard, Snorlax, Mew]


player1 = random.choice(characters)
player1_name = input('Player1 what is your name?  ')
player2 = random.choice(characters)
player2_name = input('Player2 what is your name?  ')
print('')
print(player1_name + ' you will be ' + player1.name + '!')
print('')
print(player2_name + ' you will be ' + player2.name + '!')
print('')

players = [player2,player1]
first = random.choice(players)
players2 = players.remove(first)
second = random.choice(players)

battle1 = Pokemon.battle(player1,player2)

