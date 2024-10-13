# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:29 2024

@author: bai41
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (0, n+1):
    s = s + 1/(2*i + 1) 
if n > 0:    
    print (s) 