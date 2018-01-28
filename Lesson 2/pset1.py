#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:17:36 2017

@author: normankuang
@title: Lesson 2 / Problem Set 1
"""
s = input("Enter a string: ")

numberOfVowels = 0

for letter in s:
    if (letter == 'a' or letter == 'e' or letter == 'i' or
        letter == 'o' or letter == 'u'):
        numberOfVowels += 1
    
print("Number of vowels: " + str(numberOfVowels))
