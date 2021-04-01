# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:50:30 2021

@author: willy
"""

with open("超音波_1.txt", "r", encoding="utf8") as fp:
    data = eval(fp.read())
    print(data)