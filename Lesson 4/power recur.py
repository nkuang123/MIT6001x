#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:07:46 2017

@author: normankuang
@title: Lesson 4 / Exercise: power recur
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    if (exp == 0):
        return 1
    else:
        return base * recurPower(base, exp-1)


