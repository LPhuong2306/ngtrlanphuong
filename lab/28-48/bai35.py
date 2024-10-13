# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:26 2024

@author: bai35
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (1, n+1):
    s = s + i
if n > 0:
    print (s)   