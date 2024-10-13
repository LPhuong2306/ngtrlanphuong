# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:27 2024

@author: bai37
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (2, n+1, 2):
    s = s + i
if n % 2 == 0:
    print (s)   
