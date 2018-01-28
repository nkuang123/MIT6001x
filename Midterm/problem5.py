#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:10:00 2017

@author: normankuang
@title: Midterm / Problem 5
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    
    keyList = []
    
    for key in aDict:
        if (aDict[key] == target):
            keyList.append(key)
            
    return sorted(keyList)

