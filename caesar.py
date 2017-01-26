# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:27:38 2016

@author: Kyle
"""

from helpers import alphabet_position, rotate_character
from sys import argv, exit
#print("I know know that these are the words the user typed on the command line: ", argv)


def encrypt(text, rot):
    """Caesar encryption"""    
    encrypted = ''    
    for index in range(len(text)):
        enc_char = rotate_character(text[index], rot)
        encrypted = encrypted + enc_char
    return encrypted

#Test -----------------------
'''    
print(encrypt('a', 13), 'is n')
print(encrypt('abcd', 13), 'is nopq')
print(encrypt('LaunchCode', 13), 'is YnhapuPbqr')
'''

def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        return False
    elif cl_args[1].isdigit():
        return True
    else:
        return False
    
    

def main():
    #print(argv)        
    if user_input_is_valid(argv) == False:
        print('usage: python Caesar.py n')
        exit()
    else:
        to_crypt = input('Type a message:')
        print(encrypt(to_crypt, int(argv[1])))
    
    
if __name__ ==  '__main__':
    main()