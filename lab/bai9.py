# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:02:52 2024

@author: My pc
"""

print("=========== MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")
choice = input("Moi nhap lua chon: ")
print("==============================")

menu = "Hu tieu", "Chao long", "Banh canh", "Bun rieu", "Pho bo"

if choice in ["1", "2", "3", "4", "5"]:
    print("Ban da chon: {}".format(menu[int(choice) - 1]))
else:
    print("Lua chon khong hop le!")

