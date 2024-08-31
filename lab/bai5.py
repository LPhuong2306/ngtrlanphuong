# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:57 2024

@author: My pc
"""

print("Nhập giờ, phút, giây")
h = int(input("Giờ: "))
p = int(input("Phút: "))
s = int(input("Giây: "))

if 0 <= h <= 23 and 0 <= p <= 59 and 0 <= s <= 59:
    print ("{0}:{1}:{2}".format(h, p, s))
    tong = h * 3600 + p * 60 + s
    print("Số giây được đổi là: ",tong,"giây")
else:
    print("Không hợp lệ") 