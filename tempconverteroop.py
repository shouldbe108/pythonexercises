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
    
cnv=TemperatureConverter() #create and instance

type=input("C to F enter A. F to C enter B")

if type=="A":
    tempv1=float(input("enterC temp"))
    ctemp=cnv.c_to_f(tempv1)
    print(str(ctemp)+'C')
elif type=="B":
    tempv2=float(input("enterF temp"))
    ftemp=cnv.f_to_c(tempv2)
    print(str(ftemp)+'F')
else: 
    print("invalid input restart")
