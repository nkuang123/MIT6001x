#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:23:42 2017

@author: normankuang
@title: Lesson 2 / Problem Set 2
"""

s = input("Enter")
bobCounter = 0
stringToMatch = "bob"

for i in range(0, len(s)):
    if s[i:i+len(stringToMatch)] == stringToMatch:
        bobCounter += 1
    
print("Number of times bob occurs is: " + str(bobCounter))
