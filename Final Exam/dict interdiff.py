#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:45:15 2017

@author: normankuang
@title: Final Exam / Problem 5: dict interdiff
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    def intersect_list(d1, d2):
        
        i_list = []
        d1_keys = list(d1.keys())
        d2_keys = list(d2.keys())
        
        for key in d1_keys:
            if key in d2_keys:
                i_list.append(key)
                
        return sorted(i_list)
    
    def diff_list(d1, d2):
        
        d_list = []
        d1_keys = list(d1.keys())
        d2_keys = list(d2.keys())
        
        for key in d1_keys:
            if not key in d2_keys:
                d_list.append(key)
                
        for key in d2_keys:
            if not key in d1_keys:
                d_list.append(key)
                
        return sorted(d_list)
        
        
        
    intersect_dict = {}
    diff_dict = {}
    i_list = intersect_list(d1, d2)
    d_list = diff_list(d1, d2)
    
    for key in i_list:
        intersect_dict[key] = f(d1[key], d2[key])
        
    for key in d_list:
        if key in d1:
            diff_dict[key] = d1[key]
        else:
            diff_dict[key] = d2[key]
        
    
    
    return (intersect_dict, diff_dict)

def f(a, b):
    return a + b
    
    
    

