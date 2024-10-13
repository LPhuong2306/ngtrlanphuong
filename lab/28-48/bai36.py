# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:27 2024

@author: bai36
"""

n = int(input("Nhap n: "))

if n > 0:
    s = sum(i ** 2 for i in range(1, n + 1))
    print(s)
else:
    print("Nhap lai n")
    
