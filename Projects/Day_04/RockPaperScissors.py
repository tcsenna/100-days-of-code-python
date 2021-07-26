#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:17:32 2021

@author: thonia
"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista=[rock,paper,scissors]
user_choice=int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissors?"))
if user_choice not in [0,1,2]:
  print("You typed an invalid number, you lose!")
else:
  print(lista[user_choice])
  computer_choice=random.choice([0,1,2])
  print('Computer chose:\n {}'.format(lista[computer_choice]))
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")