#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 18:17:43 2017

@author: normankuang
@title: Final Exam / Problem 4: is list permuatation
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    permutation = True
    
    for element in L1:
        if L1.count(element) != L2.count(element):
            permutation = False
    
    for element in L2:
        if L1.count(element) != L2.count(element):
            permutation = False
  
    if not permutation:
        return False
    
    most_freq_element = None
    num_of_occurance = None
    element_type = None
    
    if not L1 and not L2:
        return (most_freq_element, num_of_occurance, element_type)
    else:
        num_of_occurance = 0
        for element in L1:
            if L1.count(element) > num_of_occurance:
                 num_of_occurance = L1.count(element)
                 most_freq_element = element
                 element_type = type(element)
                 
    return (most_freq_element, num_of_occurance, element_type)
                
            
            
        
    
    
