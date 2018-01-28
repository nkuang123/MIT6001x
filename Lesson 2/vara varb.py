#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:28:47 2017

@author: normankuang
@title: Lesson 2 / Exercise: vara varb
"""

varA = "string"
varB = 1


if (type(varA) == str or type(varB) == str):
    print("string involved")
elif (varA > varB): 
    print("bigger")
elif (varA == varB):
    print("equal")
elif (varA < varB):
    print("smaller")

