#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:54:57 2017

@author: normankuang
@title: Lesson 4 / Problem Set 1
"""

def balanceForAYear(balance, annualInterestRate, monthlyPaymentRate):
    
    def balanceForAMonth(balance, annualInterestRate, monthlyPaymentRate):
        
        minMonthlyPayment = monthlyPaymentRate * balance
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBal = balance - minMonthlyPayment
        updatedBalance = monthlyUnpaidBal + (monthlyUnpaidBal * monthlyInterestRate)
                        
        return updatedBalance
        
    balanceForAYear = balance
    
    for i in range(1, 13):
        balanceForAYear = balanceForAMonth(balanceForAYear, annualInterestRate, monthlyPaymentRate)
    
    print("Remaining balance: " + str(round(balanceForAYear, 2)))

