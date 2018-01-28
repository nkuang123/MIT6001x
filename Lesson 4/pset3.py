#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:57:16 2017

@author: normankuang
@title: Lesson 4 / Exercise: Problem Set 3
"""

#Test Case 1:
#balance = 320000
#annualInterestRate = 0.2

#Test Case 2:
balance = 99999999
annualInterestRate = 0.03

initialBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = initialBalance / 12
upperBound = (initialBalance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.00000001
minPayment = (upperBound + lowerBound)/2

def calculateBalance(initialBalance, monthlyInterestRate, minPayment):
    '''
    input:
        initialBalance: starting balance
        monthlyInterestRate: Annual Interest Rate divided by 12.0
        minPayment: payment per month
    returns: the remaining balance left after one year
    '''
    unpaidBalance = initialBalance
    monthlyUnpaidBalance = initialBalance
    
    for month in range(0, 12):
        monthlyUnpaidBalance = unpaidBalance - minPayment
        unpaidBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
    return unpaidBalance

while (initialBalance > 0):
     
     currentBalance = calculateBalance(initialBalance, monthlyInterestRate, minPayment)
     
     if (abs(currentBalance) < epsilon):
         initialBalance = 0
         
     elif(currentBalance > 0):
         lowerBound = minPayment
         
     elif (currentBalance < 0):
         upperBound = minPayment
     
     
     minPayment = (upperBound + lowerBound)/2 

        
     
print("Lowest payment: " + str(round(minPayment, 2)))
    


    