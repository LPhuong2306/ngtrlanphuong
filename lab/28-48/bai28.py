# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:13:09 2024

@author: My pc
"""

N = int(input("Nhập vào số N (N phải là số nguyên dương): "))

while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại.")
    N = int(input("Nhập vào số N (N phải là số nguyên dương): "))

print(f"Tất cả ước số của {N} là: ")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
