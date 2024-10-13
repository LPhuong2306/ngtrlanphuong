# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:23:35 2024

@author: lanphuong
"""

danhsach = []
min = 979

for x in range (1, 490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                sum = x + y + z
                if sum < min:
                    min = sum
                    danhsach = [(x, y, z)]
                    
print (f"{danhsach} với bộ nghiệm (x + y + z)={min}")