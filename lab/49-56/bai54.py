# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:17:30 2024

@author: lanphuong
"""

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a, end=' ')
        a, b = b, a + b
    print ()
    
fib(5)
