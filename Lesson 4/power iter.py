#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:46:41 2017

@author: normankuang
@title: Lesson 4 / Exercise: power iter
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if (exp == 0):
        return 1
    
    result = 1
    
    while (exp >= 1):
        result *= base
        exp -= 1
        
    return result

