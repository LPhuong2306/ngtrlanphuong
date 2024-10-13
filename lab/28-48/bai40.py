# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:29 2024

@author: bai40
"""

n = int (input("Nhap so nguyen n: "))
s = 0
for i in range (1, n+1):
    s = s + 1/(2*i) 
if n > 0:    
    print (s) 