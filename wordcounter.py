# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:54:03 2023

@author: atpax
Explanation:

    The split method is used to split the input text into a list of words.
    The len function is then used to count the number of words in the list.
    The example takes user input and counts the number of words in the entered sentence.
"""

def word_counter(text):
    words = text.split()
    return len(words)

input_text= input("enter text to determine its word count \n")
result =  word_counter(input_text)
print("word count:", result)
