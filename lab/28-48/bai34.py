# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:13:52 2024

@author: My pc
"""

# Nhập vào số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))

# Kiểm tra điều kiện n là số nguyên dương
while n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
    n = int(input("Nhập vào số nguyên dương n: "))

# Kiểm tra n có phải là số nguyên tố hay không
if n == 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):  # Duyệt từ 2 đến căn bậc 2 của n
        if n % i == 0:  # Nếu n chia hết cho i, n không phải là số nguyên tố
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
