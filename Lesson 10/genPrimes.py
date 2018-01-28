#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:48:42 2017

@author: normankuang
@title: Lesson 10 / Exercise: genPrimes
"""

def genPrimes():
    
    primes = []
    number = 2
    
    while True:
        next = number
        primes.append(number)
        yield next
         
        primeFlag = False
        while not primeFlag:
            number += 1
            for prime in primes:
                if number % prime == 0:
                    primeFlag = False
                    break
                primeFlag = True
            
        
    

