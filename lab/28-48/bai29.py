# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:13:11 2024

@author: My pc
"""

N = int(input("Nhập vào số N (N phải là số nguyên dương): "))

while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại.")
    N = int(input("Nhập vào số N (N phải là số nguyên dương): "))

tong = 0
while N > 0:
    tong += N % 10  
    N //= 10       

print(f"Tổng các chữ số là: {tong}")
