# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:37:55 2024

@author: lanphuong
"""

print ("Nhập 3 số nguyên a, b và c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

dayso = [a, b, c]
print('Số lớn nhất là',max (dayso))
print('Số bé nhất là',min (dayso))
if a == b == c:
    print("Ba số bằng nhau và bằng",a|b|c)
    