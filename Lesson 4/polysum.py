#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:16:14 2017

@author: normankuang
@title: Lesson 4 / Exercise: polysum
"""

import math

def polysum(n, s):
    '''
    n: int that represents the number of sides of a polygon
    s: float that gives length of each side
    returns: the sum of the area and the square of the 
    perimeter to 4 decimal places.
    '''
    
    # HELPER FUNCTIONS
    def area(n, s):
        '''
        n: int that represents the number of sides of a polygon
        s: float that gives length of each side
        returns: the area of the polygon
        '''
        
        return ((0.25*n*(s**2))/(math.tan(math.pi/n)))
    
    def perimeter(n, s):
        '''
        n: int that represents the number of sides of a polygon
        s: float that gives length of each side
        returns: the perimeter of the polygon
        '''
        
        return n * s
    
    #polysum forumla
    polysum = area(n, s) + perimeter(n, s)**2
    
    #format() returns a string, so we cast it with float()
    return float(format(polysum, ".4f"))  
                        