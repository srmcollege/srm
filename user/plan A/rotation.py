
import matplotlib.pyplot as plt
v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro');
plt.plot(h1,h2,'-ro');
s = [0 + 0j,4 + 6j, 5 + 4j,0 + 0j];

s1 = [j.real for j in s ];
print(s1);
s2 = [j.imag for j in s ];
print(s2);

plt.plot(s1,s2,'-go');
plt.show();


import matplotlib.pyplot as plt
v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')

s = [0 + 0j,4 + 6j, 5 + 4j,0 + 0j]
T = [(x * -1j) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);


import matplotlib.pyplot as plt
v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')
plt.plot(s1,s2,'-go');
plt.show();

s = [0 + 0j,4 + 6j, 5 + 4j,0 + 0j]
T = [(x * (1j**2)) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.show();



import matplotlib.pyplot as plt
v1 = [6,-6];
v2 = [0,0];
h1 = [0,0];
h2 = [6,-6];
plt.plot(v1,v2,'-ro')
plt.plot(h1,h2,'-ro')
plt.plot(s1,s2,'-go');
plt.show();

s = [0 + 0j,4 + 6j, 5 + 4j,0 + 0j]
T = [(x * 1j) for x in s];
s1 = [j.real for j in T ];
print(s1);
s2 = [j.imag for j in T ];
print(s2);
plt.plot(s1,s2,'-go');
plt.show();

