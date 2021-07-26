#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:27:43 2021

@author: thonia
"""

for i in range(1,101):
  if i%3==0 and i%5==0:
    print('FizzBuzz!')
  elif i%3==0:
    print('Fizz!')
  elif i%5==0:
    print('Buzz!')
  else:
    print(i)