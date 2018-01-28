#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:53:05 2017

@author: normankuang
@title: Lesson 6 / Exercise: biggest
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    biggestKey = ''
    biggestValue = 0
    
    for key in aDict:
        if (len(aDict[key]) > biggestValue):
            biggestKey = key
            biggestValue = len(aDict[key])
            
    return biggestKey

