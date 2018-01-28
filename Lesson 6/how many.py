#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 21:48:18 2017

@author: normankuang
@title: Lesson 6 / Exercise: how many
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    
    for values in aDict.values():
        total += len(values)
        
    return total
