# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:28 2024

@author: bai38
"""

n = int (input("Nhap so nguyen n: "))
s = 1
for i in range (1, n+1):
    s = s * i
if n > 0 and n % 2 != 0:
    print (s)  