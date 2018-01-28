#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:13:37 2017

@author: normankuang
@title: Midterm / Problem 3
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if (b > x):
        return 0
    
    base = 1
    
    while ((b**base) < x):
        if ((b**(base+1) > x)):
            break;
        base += 1
    
    return base

myLog(80, 3)