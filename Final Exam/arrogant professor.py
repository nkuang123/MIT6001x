#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:02:46 2017

@author: normankuang
@title: Final Exam / Problem 6: arrogant professor
"""

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Person.say(self, 'It is obvious that ' + Person.say(self, stuff))
    def lecture(self, stuff):
        return "It is obvious that " + Person.say(self, stuff)
    
p = Person('eric')
l = Lecturer('eric')
prof = Professor('eric')
ap = ArrogantProfessor('eric')

