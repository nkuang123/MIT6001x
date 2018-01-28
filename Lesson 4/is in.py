#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:00:19 2017

@author: normankuang
@title: Lesson 4 / Exercise: is in
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if (len(aStr) == 0):
        return False
    
    middleChar = aStr[len(aStr)//2]
    
    if (len(aStr) == 1):
        return char == aStr
    elif (char < middleChar):
        return isIn(char, aStr[:len(aStr)//2])
    else:
        return isIn(char, aStr[len(aStr)//2:])
    
    

