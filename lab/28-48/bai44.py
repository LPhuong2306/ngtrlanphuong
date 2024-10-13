# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:59:44 2024

@author: bai44
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (0, n+1):
    s = s + (2*i + 1)/(2*i + 2) 
if n > 0:    
    print (s) 