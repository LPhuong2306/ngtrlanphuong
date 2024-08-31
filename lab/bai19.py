# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:32 2024

@author: lanphuong
"""

print ("Nhập vào 4 số nguyên")
a = int (input("a = "))
b = int (input("b = "))
c = int (input("c = "))
d = int (input("d = "))

if a <= b and a <= c and a <= d:
    print ("Số nhỏ nhất là:",a)
elif b < a and b <= c and b <= d:
    print ("Số nhỏ nhất là:",b)
elif c < a and c < b and c <= d:
    print ("Số nhỏ nhất là:",c)    
elif d < a and d < c and d < b:
    print ("Số nhỏ nhất là:",d)
    