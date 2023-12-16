# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:58:59 2023

@author: atpax
Explanation:

    The TemperatureConverter class provides methods to convert temperatures between Celsius and Fahrenheit.
    The example usage demonstrates converting a temperature from Celsius to Fahrenheit.
"""

class TemperatureConverter:
    def c_to_f(self, celsius):
        return (celsius*(9/5)+32)
    def f_to_c(self, fahrenheit):
        return (fahrenheit - 32)*(5/9)
    

