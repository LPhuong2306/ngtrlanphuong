# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:27:17 2024

@author: lanphuong
"""

print("Nhập vào số có hai chữ số:")
n = int(input ("n = "))
a = n // 10
b = n % 10
s = a + b
if 10 <= n <= 99:
    print ("Tổng của 2 chữ số là: ", s)
    



