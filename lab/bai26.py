# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:08:34 2024

@author: lanphuong
"""

#a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
bien = 0

if a > b:
    bien = a
    a = b
    b = bien

if a > c:
    bien = a
    a = c
    c = bien

if b > c:
    bien = b
    b = c
    c = bien

print("Số theo thứ tự tăng dần: {0}, {1}, {2}".format(a, b, c))

#b

N = int(input("Nhập vào số nguyên N: "))
n_str = str(N)
sorted_n_str = ''.join(sorted(n_str))
sorted_n = int(sorted_n_str)

print("Số sau khi sắp xếp các chữ số theo thứ tự tăng dần là:", sorted_n)
