#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:09:13 2017

@author: normankuang
@title: Lesson 4 / Exercise: Problem Set 2
"""

#Test Case 1:
#balance = 3329      
#annualInterestRate = 0.2

#Test Case 2:
balance = 0
annualInterestRate = 0.2

#Test Case 3:
#balance = 3926
#annualInterestRate = 0.2

monthlyInterestRate =  annualInterestRate / 12.0
monthlyUnpaidBalance = 0
initBalance = balance
minPayment = 0


while (initBalance >= 0):
    
    minPayment += 10
    unpaidBalance = initBalance
    monthlyUnpaidBalance = initBalance
    
    for month in range(0, 12):
        monthlyUnpaidBalance = unpaidBalance - minPayment
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
    if (unpaidBalance <= 0):
        initBalance = unpaidBalance
    
print("Lowest payment: " + str(minPayment))
        
        
        
    