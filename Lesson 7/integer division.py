#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:58:01 2017

@author: normankuang
@title: Lesson 7 / Exercise: integer division
"""

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    
    while x >= a:
        count += 1
        x = x - a
        
    return count


