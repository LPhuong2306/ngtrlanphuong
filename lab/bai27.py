# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:37:51 2024

@author: lanphuong
"""

print ("hình vuông (v), hình chữ nhật (n) và hình tròn (t)")
chon = input("Vui lòng chọn 1 trong các hình trên bằng cách nhập các ký tự v, n, t tương ứng với mỗi hình: ")

if chon == "v":
    #Hinh vuong
    print ("Tính chu vi và diện tích của hình vuông")
    a = float(input ("Nhập độ dài cạnh hình vuông: "))
    if a > 0:
        chuvi = a * 4
        dientich = a ** 2
        print("Hình vuông có chu vi bằng",chuvi,"và diện tích bằng",dientich)
    

elif chon == "n":
    #Hinhchunhat
    print ("Tính chu vi và diện tích của hình chữ nhật")
    print ("Nhập chiều dài và chiều rộng hình chữ nhật: ")
    dai = float(input("Chiều dài: "))
    rong = float(input("Chiều rộng: "))
    p = (dai + rong) * 2
    s = dai * rong
    if dai > 0 and rong > 0 and dai != rong:
        print("Hình chữ nhật có chu vi bằng",p,"và diện tích bằng",s)
    elif dai == rong:
        print ("Đây là hình vuông và có chu vi bằng",p,", diện tích bằng",s)
    

elif chon == "t":
    #Hinhtron
    print ("Tính chu vi và diện tích của hình tròn")
    r = float(input("Nhập bán kính hình tròn: "))
    pi = 3.14
    if r > 0:
        c = 2 * pi * r
        dt = pi * pow (r, 2)
        print("Hình tròn có chu vi bằng", c,"và diện tích bằng", dt)
        round (c, 3)
    
else:
    print ("Không có hình tương ứng")
    
