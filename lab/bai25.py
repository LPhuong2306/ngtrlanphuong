# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:37:53 2024

@author: lanphuong
"""

str1 = input ("Nhập vào 1 chữ cái: ")
s = str1.swapcase()
if len(s) == 1:
    print ('Chữ cái được đổi định dạng thành', s)
else:
    print("Không hợp lệ")
    