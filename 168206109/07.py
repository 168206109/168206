# -*- coding: utf-8 -*-
import math
 
for i in range(100, 1000):
    x = math.floor(i/100)  #获得百位数
    y = math.floor((i - x*100)/10)  #获得十位数
    z = i - math.floor(i/10) *10  #获得个位数
    if i == x**3 + y**3 + z**3:
        print(i, end=', ')
