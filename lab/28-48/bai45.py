# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:52:28 2024

@author: bai45
"""

n = int (input("Nhap n: "))
x = int (input("Nhap x: "))

tong = 0
mau = 0
for i in range (1, n+1):
    mau = mau + i
    tong = tong + (x ** i) / mau
print(tong)

    