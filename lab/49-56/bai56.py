# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 00:05:40 2024

@author: lanphuong
"""

import math

def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh')
    tinh_ = kwargs.get('tinh')

    if hinh == 'vuong':
        canh = args[0]
        print(4 * canh if tinh_ == 'cv' else canh * canh)
    elif hinh == 'chu_nhat':
        dai, rong = args
        print(2 * (dai + rong) if tinh_ == 'cv' else dai * rong)
    elif hinh == 'tron':
        r = args[0]
        print(2 * math.pi * r if tinh_ == 'cv' else math.pi * r ** 2)

# Ví dụ sử dụng hàm:
tinh(10, hinh='vuong', tinh='cv')        # Hình vuông, tính chu vi
tinh(50, hinh='vuong', tinh='dt')        # Hình vuông, tính diện tích
tinh(18, hinh='tron', tinh='cv')         # Hình tròn, tính chu vi
tinh(20, 30, hinh='chu_nhat', tinh='cv')   # Hình chữ nhật, tính chu vi
