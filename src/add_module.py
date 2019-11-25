# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:14:24 2019

@author: lennie
"""

class AddClass():
    def __init__(self):
        pass
    
    def Add(self,x,y):
        try:
            return x+y
        except TypeError:
            return None
    