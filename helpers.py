# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 15:07:04 2016

@author: Kyle
"""

def alphabet_position(letter):
    """ recieves a string with only one alphabetic charactyer and returns a 0 based position within the alphabet. 
        Should be case-INsensitive"""
    letter = letter.lower()
    position = ord(letter) - ord('a')
    return position
    
#test -------------------------
'''
print (alphabet_position('a'), 'is 0')
print (alphabet_position('A'), 'is 0')
print (alphabet_position('b'), 'is 1')
print (alphabet_position('y'), 'is 24')
print (alphabet_position('z'), 'is 25')
print (alphabet_position('Z'), 'is 25')
'''

def rotate_character(char, rot):
    """ recieves a character and an integer, then returns a new character, rotated to the right"""
    
    def small_rotate(char, rot):
        position = (int(alphabet_position(char)) + rot) %26 +97
        new_char = chr(position)
        return new_char
    
    if 91 > ord(char) > 65:  #is uppercase
        char = char.lower()
        new_char = small_rotate(char, rot)
        new_char = new_char.upper()
        return new_char
    elif 123 > ord(char) > 96: #is lowercase
        new_char = small_rotate(char, rot)
        return new_char
    else:
        return char
        
#test -------------------------       
'''
print(rotate_character('a', 13), 'is n')
print(rotate_character('a', 14), 'is o')     
print(rotate_character('a', 0), 'is a')
print(rotate_character('c', 26), 'is c')
print(rotate_character('c', 27), 'is d')
print(rotate_character('Z', 2), 'is B')
print(rotate_character('!', 37), 'is !')
print(rotate_character('6', 14), 'is 6')
 '''  
