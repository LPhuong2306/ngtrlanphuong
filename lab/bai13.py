# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:40:51 2024

@author: lanphuong
"""


ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))

a = "{0}/{1}/{2}".format(ngay, thang, nam)
b = "{0}/{1}/{2}".format(ngay, thang, nam % 100)
c = "{0}/{1}/{2}".format(ngay, thang, nam)

print("Ngày/tháng/năm:", a)
print("Ngày/tháng/năm:", b)
print("Năm/tháng/ngày:", c)

a_nguoc = input("Nhập ngày/tháng/năm (ví dụ: 20/8/1990): ")
ngay, thang, nam = map(int, a_nguoc.split('/'))
print("Ngày: {0}, Tháng: {1}, Năm: {2}".format(ngay, thang, nam))

b_nguoc = input("Nhập ngày/tháng/năm (ví dụ: 20/8/90): ")
ngay, thang, nam = b_nguoc.split('/')
nam = int("19" + nam) if int(nam) > 50 else int("20" + nam)  
print("Ngày: {0}, Tháng: {1}, Năm: {2}".format(ngay, thang, nam))

c_nguoc = input("Nhập năm/tháng/ngày (ví dụ: 1990/8/20): ")
nam, thang, ngay = map(int, c_nguoc.split('/'))
print("Ngày: {0}, Tháng: {1}, Năm: {2}".format(ngay, thang, nam))
