# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = [6,7,-3,4,5];
y = [8,5,6,7,-3];

def addition(x,y):
    list1 = [x[i] + y[i] for i in range(0,len(x))];
    print(f"addition of both vectors is {list1}");

addition(x,y);

