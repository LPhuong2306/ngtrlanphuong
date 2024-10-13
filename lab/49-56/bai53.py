# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:53:09 2024

@author: bai53
"""

#a
def tong_dso(n):
    s = 0
    for i in range (1, n+1):
        s += i
    return s

#b
def tong_socuoi2(n):
    dso = [(i * 10 + 2) for i in range(1, n + 1)]
    tong = sum(dso)   
    return tong, dso
#c
def tong_nghich_dao(n):
    return sum(1 / i for i in range(1, n + 1))

#d
def tong_giai_thua(n):
    tongso = 0
    for i in range(1, n + 1):
        x = 1
        for j in range(1, i + 1):
            x *= j  
        tongso += x 
    return tongso

#e
def tich_day_so(n):
    tich = 1
    for i in range(1, n + 1):
        tich *= i
    return tich

if __name__ == '__main__':
    print(tong_dso(5)) #a
    tong, dso = tong_socuoi2(2) #b
    print(tong)
    print (tong_nghich_dao(3)) #c
    print(tong_giai_thua(4)) #d
    print(tich_day_so(2)) #
    