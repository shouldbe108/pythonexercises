# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 00:49:59 2023

@author: atpax

Explanation:

    The open function is used to open a file, and the with statement ensures proper handling of resources.
    Writing is done using the "w" mode, and reading is done using the "r" mode.
    This example writes a line of text to a file and then reads and prints the file's content.
"""

#writing to a file
with open("example.txt", "w") as file:
    file.write("This is a sample text.")

with open("example.txt","r") as file:
    content =file.read()
    print("File content:", content)