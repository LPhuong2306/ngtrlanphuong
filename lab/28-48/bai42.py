# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:30 2024

@author: bai42
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (1, n+1):
    s = s + 1/(i*(i + 1)) 
if n > 0:    
    print (s) 