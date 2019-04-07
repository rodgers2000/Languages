# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Mike:
    
    def func1(self, index):
        
        if index == 1:
            return 1
        
        return self.func1(index - 1)
    
mjr = Mike()
mjr.func1(5)
        
