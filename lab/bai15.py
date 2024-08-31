# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:37:37 2024

@author: lanphuong
"""

print ("Nhập 2 số a, b: ")
a = float(input("a = "))
b = float(input("b = "))

tu = a + b
mau = (pow (a, 1/3) + pow (b, 1/3))
sotru = tu / mau
sobitru = pow (a * b, 1/3)
sobichia = (pow (a, 1/3) - pow (b, 1/3))
sbc = pow (sobichia, 2)

gtri = (sotru - sobitru) / sbc

print ("Giá trị của biểu thức là: ", gtri)
