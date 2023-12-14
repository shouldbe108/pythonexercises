# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:18:31 2023

@author: atpax
"""
#calculator OOP
class Calculator:
    def add(self, x, y):
        return x+y
    def subtract(self, x, y):
        return x-y
    def divide(self, x, y):
        if y!=0:
            return x/y
        else:
            return "cannot divide by zero"
    def multiply(self, x, y):
        return x*y
    
calculator = Calculator()
result = calculator.add(5,3)
print("Addition",result)





