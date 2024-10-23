# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#COMPLEX NUMBER
print(type(1+2j))
x=1+3j
print(x)
y=4+5j
print(y)
print(x+y)
print((x-1)**2)
print(x.real)
print(y.imag)
print(x.conjugate())
print(abs(x))
print(abs(3+4j))

#original
import matplotlib.pyplot as plt
s=[1+1j,1+3j,1+5j,5+5j,5+3j,1+3j]
x=[x.real for x in s]
print(x)
y=[y.imag for y in s]
print(y)
plt.plot(x,y,'go-')
plt.show()

#translation
s1=[x+(1+2j)for x in s]
print(s1)
x=[x.real for x in s1]
print(x)
y=[y.imag for y in s1]
print(y)
plt.plot(x,y,'yo-')
plt.show()

#scaling
s1=[x*(1+2j) for x in s]
x1=[x.real for x in s1]
print(x1)
y1=[y.imag for y in s1]
print(y1)
plt.plot(x1,y1,'ro-')
plt.show()

#rotation 90 degree
p1=[x*1j for x in s]
print(p1)
x2=[x.real for x in p1]
print(x2)
y2=[y.imag for y in p1]
print(y2)
plt.plot(x2,y2,'go-')
plt.show()

#rotation 180 degree
p2=[x*1j**2 for x in s]
print(p2)
x2=[x.real for x in p2]
print(x2)
y2=[y.imag for y in p2]
print(y2)
plt.plot(x2,y2,'go-')
plt.show()

#rotation 270 degree
p3=[x*1j**3 for x in s]
print(p3)
x2=[x.real for x in p3]
print(x2)
y2=[y.imag for y in p3]
print(y2)
plt.plot(x2,y2,'go-')
plt.show()


