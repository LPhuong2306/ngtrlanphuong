# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:42 2024

@author: lanphuong
"""

print("Kiểm tra tính hợp lệ của giờ, phút, giây")
h = int(input("Giờ: "))
p = int(input("Phút: "))
s = int(input("Giây: "))

if 0 <= h <= 23 and 0 <= p <= 59 and 0 <= s <= 59:
    print ("Hợp lệ")
else:
    print("Không hợp lệ")
    