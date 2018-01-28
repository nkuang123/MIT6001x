#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:18:11 2017

@author: normankuang
@title: Lesson 4 / Exercise: gcd iter
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    
    if (a < b):
        gcd = a
    else:
        gcd = b
        
    while (gcd > 1):
        if (a % gcd == 0 and b % gcd == 0):
            return gcd
        gcd -= 1
    
    return gcd
    
    

