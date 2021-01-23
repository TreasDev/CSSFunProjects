from math import pow
g = 9.81
t = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
u = 0
s = []
print('distance [m]')
for i in range(len(t)):
    s.append(u*t[i] + (g*pow(t[i],2))/2)
    print('%.2f' % s[i])
print('distance [%]')
for i in range(len(s)):
    print('%.2f' % (s[i]/max(s)))
