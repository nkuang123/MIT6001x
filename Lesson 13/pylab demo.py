#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:51:34 2017

@author: normankuang
@title: Lesson 13 / Pylab Demonstration
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
plt.figure("Linear")
plt.plot(mySamples, myLinear)
plt.figure("Quadratic")
plt.plot(mySamples, myQuadratic)
plt.figure("Cubic")
plt.plot(mySamples, myCubic)
plt.figure("Exponential")
plt.plot(mySamples, myExponential)
    


