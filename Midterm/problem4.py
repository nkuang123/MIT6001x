#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:06:53 2017

@author: normankuang
@title: Midterm / Problem 4
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    subList = []
    
    for string in aList:
        if (len(string) < 4):
            subList.append(string)
            
    return subList