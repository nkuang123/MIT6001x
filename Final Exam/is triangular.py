#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:58:05 2017

@author: normankuang
@title: Final Exam / Problem 3: is triangular
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triangular_list = []
    triangular_counter = 0
    
    for i in range(1, k+1):
        triangular_counter += i
        triangular_list.append(triangular_counter)
        
        if k in triangular_list:
            return True
        
    return False
            
is_triangular(2)


        
            



