# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:37:13 2023

@author: atpax
"""

#number guessing 1-10 oop
import random
def guess_the_number():
    secret_number = random.randint(1,10)
    print(secret_number)
    attempts = 0
    
    while True:
        guess = int(input("enter your guess: " ))
        attempts=attempts+1
        
        if guess == secret_number:
            print("correct")
            print(attempts)
            break
        elif guess < secret_number:
            print("too low")
        else:
            print("too high")
            
