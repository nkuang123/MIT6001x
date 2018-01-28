#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:20:11 2017

@author: normankuang
@title: Lesson 3 / Exercise: guess my number
"""

highBound = 100
lowBound = 0
guess = int((highBound + lowBound) / 2)

print("Please think of a number between 0 and 100!")

while True:
    guess = int((highBound + lowBound) / 2)
    
    print("Is your secret number " + str(guess) + "?")
    
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if (userInput != "h" and userInput != "l" and userInput != "c"):
        print("Please enter a valid response.")
    elif(userInput == 'h'):
        highBound = guess
    elif(userInput == 'l'):
        lowBound = guess
    else:
        break
    
print("Game over. Your secret number was " + str(guess))
        
    
    
        



