#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:32:22 2017

@author: normankuang
@title: Midterm / Problem 7
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    
    scoreDict = {}
    scoreList = []
    distanceCounter = 0
    
    # Mapping each letter to its score.
    for letter in word:
        if (letter in scoreDict):
            scoreDict[letter + str(distanceCounter)] = scoreForALetter(letter.lower(), distanceCounter)
        else:
            scoreDict[letter] = scoreForALetter(letter.lower(), distanceCounter)
        distanceCounter += 1
        
    scoreList = list(scoreDict.values())
    scoreList.sort()
    
    return f(scoreList[-1], scoreList[-2])
    
#HELPER FUNCTION
def scoreForALetter(character, distance):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # We need to add one to the index, because we are basing this on one-index, 
    #  not zero-index
    return (alphabet.index(character)+1) * distance


    
        
 
