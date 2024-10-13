# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:13:18 2024

@author: My pc
"""

import math

n = int(input("Nhập vào số nguyên dương n: "))

while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    n = int(input("Nhập vào số nguyên dương n: "))

can_bac_2 = math.isqrt(n)  
if can_bac_2 * can_bac_2 == n:
    print(f"{n} là số chính phương.")
else:
    print(f"{n} không phải là số chính phương.")
