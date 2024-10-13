# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:02:27 2024

@author: lanphuong
"""

dai = 10  
rong = 4

chu_vi = 2 * (dai + rong)
print("Chu vi của hình chữ nhật là:", chu_vi)

dien_tich = dai * rong
print("Diện tích của hình chữ nhật là:", dien_tich)

print("Hình chữ nhật:")
for i in range(rong):
    print("*" * dai)

