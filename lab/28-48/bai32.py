# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:13:56 2024

@author: lanphuong
"""

sokm = int(input('Nhập vào số km đã đi được: '))
tong=0
if sokm == 1:
    tong = sokm * 15000
elif 2 <= sokm <= 5:
    tong= 15000 + (sokm - 1) * 13500
elif sokm >= 6:
    tong = 15000 + (sokm - 4) * 13500 + sokm * 11000
elif sokm >= 120:
    tong = (15000 + (sokm - 4) * 13500 + sokm * 11000) * 0.9
print (' Số km đã đi là: ', tong)
