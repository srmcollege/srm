
x = 4 - 3j;
print(x.real)
print(x.imag)
print(x.conjugate())

print(abs(x))

import matplotlib.pyplot as plt

s = [0 + 0j,4 + 6j,  5 + 4j,0 + 0j]

s1 = [j.real for j in s ]
print(s1)
s2 = [j.imag for j in s ]
print(s2)

plt.plot(s1,s2,'-go')
plt.show()


