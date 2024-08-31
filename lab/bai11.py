# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:19:37 2024

@author: lanphuong
"""

str1 = input ("Nhập vào 1 ký tự: ")
s = str1.upper()
if len(s) == 1 & str1.islower():
    print ('Ký tự hoa là', s)
else:
    print("Không hợp lệ")
    
    
