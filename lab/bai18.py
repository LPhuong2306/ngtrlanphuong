# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:47 2024

@author: lanphuong
"""

print("Nhập thời gian thứ nhất:")
h1 = int(input("Gio: "))
m1 = int(input("Phut: "))
s1 = int(input("Giay: "))

print("\nNhập thời gian thứ hai:")
h2 = int(input("Gio: "))
m2 = int(input("Phut: "))
s2 = int(input("Giay: "))

tonggiay1 = h1 * 3600 + m1 * 60 + s1
tonggiay2 = h2 * 3600 + m2 * 60 + s2

tong = tonggiay1 + tonggiay2
htong = tong // 3600
mtong = (tong % 3600) // 60
stong = tong % 60

hieu = abs(tonggiay1 - tonggiay2)
hhieu = hieu // 3600
mhieu = (hieu % 3600) // 60
shieu = hieu % 60

print("\nTổng hai thời gian:")
print("{0} gio, {1} phut, {2} giay".format(htong, mtong, stong))

print("\nHiệu hai thời gian:")
print("{0} gio, {1} phut, {2} giay".format(hhieu, mhieu, shieu))
