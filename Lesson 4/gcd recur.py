#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:05:16 2017

@author: normankuang
@title: Lesson 4 / Exercise: gcd recur
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a % b)

