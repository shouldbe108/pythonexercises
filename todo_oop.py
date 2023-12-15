# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:26:00 2023

@author: atpax
"""

#todo list OOP 
class ToDoList:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def view_tasks(self):
        if not self.tasks:
            return "no tasks"
        else:
            return "\n".join(self.tasks)
        