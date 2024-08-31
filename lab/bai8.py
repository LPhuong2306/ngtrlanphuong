# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:48:20 2024

@author: lanphuong
"""

print ("Nhập cân nặng của bạn: ")
nang = float(input("Cân nặng (kg): "))
print ("Nhập chiều cao của bạn: ")
cao = float(input("Chiều cao (m): "))

bmi = nang / pow (cao, 2)
 
print ("Chỉ số BMI của bạn là: ", bmi)

