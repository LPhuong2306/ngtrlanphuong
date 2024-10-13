# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:22:04 2024

@author: lanphuong
"""

import math

#a. Phương thức tính căn bậc x của số n
def can_bac_n(x,n):
    return x ** (1/n)

#b. Phương thức trả về số đảo
# cách 1. Chuỗi hoặc chữ số, giữ lại số 0 đằng trước
def dao_so(n):
    return str(n)[::-1]
# cách 2. số: mất số 0 đăng trước
def dao(n):
    dao = 0
    while n > 0:
        dao = dao * 10 + n % 10
        n //= 10
    return dao

#c. Phương thức kiểm tra có phải số chính phương 
def ktra_chinhphuong(n):
    return int(math.sqrt(n))**2 == n

#d.  Phương thức kiểm tra có phải là số nguyên tố 
def ktra_nguyento(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

#e. Phương thức tính tích các chữ số lẻ. 
def tichsole(n):
    tich = 1
    for i in str(n):            #str là tính chữ số lẻ phải dùng str(string)
        tich *= int(i)          #nếu đề không nói là CHỮ SỐ thì dùng for i ..... range (1, n+1)
    return tich

#f. Phương thức tính tổng các số nguyên tố nhỏ hơn n 
def tong_ngto_nho_n(n):
    tong_ngto = 0
    for i in range (2, n):
        if ktra_nguyento(i):
            tong_ngto += i
    return tong_ngto

#g. Phương thức tính tổng các số chính phương nhỏ hơn n. 
def tong_chinhphuong(n):
    tong_cp = 0
    for i in range (1, n):
        if ktra_chinhphuong(i):
            tong_cp += i
    return tong_cp

#h. Phương thức tính tổng các ước số dương của n.
def tong_uoc(n):
    tong = 0
    for i in range (1, n+1):
        if n%i == 0:
            tong += i
    return tong

if __name__ == '__main__':
    print (can_bac_n(8, 3))
    print (dao_so(123450))
    print (dao(123450))
    print (ktra_chinhphuong(2))
    print (ktra_nguyento(4))
    print (tichsole(3))
    print (tong_ngto_nho_n(7))
    print (tong_chinhphuong(9))
    print (tong_uoc(12))

        