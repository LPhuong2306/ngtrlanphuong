# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:06:57 2024

@author: lanphuong
"""

print ("Nhập vào biển số xe của bạn (4 số): ") 
n = int(input ())
#
d = n % 10
n = n // 10
#n3
c = n % 10
n = n // 10
#n2
b = n % 10
n = n // 10
#n1
a = n
#tong4so
s = (a + b + c + d)
s1 = s // 10
s2 = s % 10
nut = s1 + s2
print ("Số xe bạn được",nut,"nút")




