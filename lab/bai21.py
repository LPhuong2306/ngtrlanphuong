# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:48 2024

@author: My pc
"""

so_viet = ["Khong", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]

so_nhap = int(input("Nhap mot so: "))

if 0 <= so_nhap <= 9:
  print(so_viet[so_nhap])
else:
  print("Khong doc duoc")
  