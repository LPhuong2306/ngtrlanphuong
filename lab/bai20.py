# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:45 2024

@author: My pc
"""

a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

if a >= b and a >= c:
    somax = a        
elif b >= a and b >= c:
    somax = b
else:
    somax = c

print("So lon nhat la:", somax)
