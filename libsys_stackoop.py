# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:44:32 2023

@author: atpax
library simulation series to learn Data structures 
Stack Implementation (OOP):

    The Stack class follows the Last In, First Out (LIFO) principle, where the last item added is the first one to be removed.

"""
class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        
#stack implementation 
class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,item):
            self.items.append(item)
            
    def pop(self):
            if not self.is_empty():
                return self.items.pop()
            else:
                return None
        
    def is_empty(self):
            return len(self.items)==0
        
#example of stack usage:
    
if __name__ == "__main__":
    #create books:
    book1 = Book("Python Crash Course", "Eric Matthes")
    book2 = Book("Clean Code", "Robert C. Martin")
    book3 = Book("Data Structures and Algorithms", "Michael T. Goodrich")
    
    #stack usage:
    book_stack = Stack()
    book_stack.push(book1)
    book_stack.push(book2)
    popped_book = book_stack.pop()
    print(f"Popped book: {popped_book.title} by {popped_book.author}")
