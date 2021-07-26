#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:28:10 2021

@author: thonia
"""

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
print("Welcome to the PyPassword Generator!")
nlet = int(input("How many letters would you like in your password?\n"))
nsym = int(input("How many symbols would you like?\n"))
nnum = int(input("How many numbers would you like?\n"))
total=nlet+nsym+nnum
stri='l'*nlet+'n'*nnum+'s'*nsym
L=list(stri)
random.shuffle(L)
for i in range(len(L)):
  if L[i]=='l':
    L[i]=random.choice(letters)
  elif L[i]=='n':
    L[i]=random.choice(numbers)
  else:
    L[i]=random.choice(symbols)
L=''.join(L)
print('Your new powerful password is {}  !'.format(L))