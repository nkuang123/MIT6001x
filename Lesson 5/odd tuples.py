#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:06:11 2017

@author: normankuang
@title: Lesson 5 / Exercise: odd tuples
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    resultTup = ()
    
    for counter in range (len(aTup)):
        if (counter % 2 == 0):
            resultTup += (aTup[counter], )
        
        
        
    return resultTup

