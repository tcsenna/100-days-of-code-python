#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:03:50 2021

@author: thonia
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests



name=name1+name2
name=name.lower()
centenas=0
unidades=0
for i in 'true':
    centenas+=name.count(i)
for i in 'love':
    unidades+=name.count(i)
chance=int(str(centenas)+str(unidades))
if chance<10 or chance>90:
  print("Your score is {}, you go together like coke and mentos.".format(chance))
elif chance>40 and chance<50:
  print("Your score is {}, you are alright together.".format(chance))
else:
  print("Your score is {}.".format(chance))

