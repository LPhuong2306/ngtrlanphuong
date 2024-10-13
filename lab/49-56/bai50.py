# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:23:47 2024

@author: lanphuong
"""

def kiem_tra(n):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2==0:
        return 1
    return 0
print(kiem_tra(4))
