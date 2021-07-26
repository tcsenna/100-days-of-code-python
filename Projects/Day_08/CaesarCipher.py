#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:21:21 2021

@author: thonia
"""

#Caesar Cipher Challenge
direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def enc_dec(text=text,direction=direction,shift=shift):
  ascii_val=[ord(i) for i in text]
  if direction=='e':
    new_ascii=[j+shift for j in ascii_val]
    new_text="".join([chr(i) for i in new_ascii])
    print(new_text)
  elif direction=='d':
    enc_dec(text=text,direction='e',shift=-shift)
