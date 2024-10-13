# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:23:47 2024

@author: lanphuong
"""

def ktra_giatri():
    gtri = input('nhap gia tri ')
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -86 <= gtri <= 90:
        return gtri
    print('khong hop le, nhap lai')
    return ktra_giatri()
print(ktra_giatri())
