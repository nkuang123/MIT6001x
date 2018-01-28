#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 21:01:08 2017

@author: normankuang
@title: Lesson 12 / Exercise: bogo sort
"""

def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)

def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True