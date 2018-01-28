#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:03:36 2017

@author: normankuang
@title: Lesson 10 / genFib
"""

def genFib():
    fibn_1 = 1 
    fibn_2 = 0
    
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next