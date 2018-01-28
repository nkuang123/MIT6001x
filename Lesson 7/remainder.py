#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:21:59 2017

@author: normankuang
@title: Lesson 7 / Exercise: remainder
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    print(x)
    print(a)
    if x == a:
        print(str(x) + "==" + str(a))
        return 0
    elif x < a:
        print(str(x) + "<" + str(a))
        return x
        print(str(x) + "<" + str(a))
    else:
        return rem(x-a, a)