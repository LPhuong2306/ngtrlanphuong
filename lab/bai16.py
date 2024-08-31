# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:54 2024

@author: lanphuong
"""

print("Nhập giờ, phút, giây")
h = int(input("Giờ: "))
p = int(input("Phút: "))
s = int(input("Giây: "))

if 0 <= h <= 23 and 0 <= p <= 59 and 0 <= s <= 59:
    print ("{0}h{1}p{2}s".format(h, p, s))
    tong = h * 3600 + p * 60 + s
    print("Số giây được đổi là: ",tong,"giây")
else:
    print("Không hợp lệ")    