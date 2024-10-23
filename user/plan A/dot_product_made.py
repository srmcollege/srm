# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 18:23:35 2024

@author: SERVER
"""

x = [9,7,-8,24,7];
y = [7,8,6,45,-3];

def addition(x,y):
    list1 = [(x[i] * y[i]) for i in range(0,len(x))];
    sum1 = sum(list1);
    print(f"dot products of the vectors is {sum1}");

addition(x,y);


