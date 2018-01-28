#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:38:22 2017

@author: normankuang
@title: Lesson 2 / Problem Set 3
"""

s = input("Enter a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
longestString = ""

for char in s:
    
    currentString = char
    indexOfChar = s.index(char)
    
    for otherChar in s[indexOfChar+1:]:
        
        if (alphabet.index(currentString[-1]) <= alphabet.index(otherChar)):
            currentString += otherChar
        else:
            break;
    
    if (len(currentString) > len(longestString)):
        longestString = currentString

print("Longest substring in alphabetical order is: " + longestString)
        
    
    
        
    
