#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:57:09 2021

@author: thonia
"""
#Hangman- Portuguese version
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   


lwords=['aniversario','xicara','janela','gato','casaco','moderado','chiclete','chuveiro','sobrancelha','impressora']
palavra=random.choice(lwords)
status=['_' for x in range(len(palavra))]
print(f'{logo} \n')
vida=6
print(stages[vida])
print(' '.join([i for i in status]))
while '_' in status and vida>0:
  letra=input('Digite uma letra! Duvido vc acertar! \n').lower()
  if letra in status:
    print('Vc ja tinha adivinhado esta letra!')
  if letra not in palavra:
    vida-=1
    print(f'Vc chutou {letra} e errou! ')
  else:
    for i in range(len(palavra)):
      if palavra[i]==letra:
        status[i]=letra
  print(' '.join([i for i in status]))
  print(stages[vida])
  
if '_' in status:
  print(f'Vc perdeu! A palavra era {palavra}!')
else:
  print('Parabens! Vc acertou o enigma!!! ')