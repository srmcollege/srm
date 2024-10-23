
import matplotlib.pyplot as plt

v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')

s = [6 - 0j,-6 + 6j, -6 - 6j,6 - 0j]
T = [x for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.plot(s1,s2,'-go');
plt.show();




import matplotlib.pyplot as plt\

v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')


s = [6 - 0j,-6 + 6j, -6 - 6j,6 - 0j]
T = [(x * 1/2) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.plot(s1,s2,'-go');
plt.show();



import matplotlib.pyplot as plt\

v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')

s = [6 - 0j,-6 + 6j, -6 - 6j,6 - 0j]
T = [(x * 1/3) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.plot(s1,s2,'-go');
plt.show();



import matplotlib.pyplot as plt\

v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')

s = [6 - 0j,-6 + 6j, -6 - 6j,6 - 0j]
T = [(x * 2) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.plot(s1,s2,'-go');
plt.show();



