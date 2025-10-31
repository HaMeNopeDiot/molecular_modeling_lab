"""
The Lennard-Jones potential
SCIPY.OPTIMIZE: FMIN & MINIMIZE
"""
import numpy as np
from numpy import linalg as LA
from scipy.optimize import fmin, minimize
import matplotlib.pyplot as plt


def U(r):
    # dimensionless units
    w = r**(-6)
    return 4.0*(w*w - w)

nt = 100
x = np.linspace(1.0e-5, 2.5, nt)
plt.plot(x, U(x), color="red", linewidth=4)
plt.title('The Lennard-Jones potential')
plt.xlabel('r')
plt.ylabel('U(r)')
plt.xlim(0.0, 2.5)
plt.ylim(-1.5, 5.0)
plt.grid(True)
plt.savefig("Lennard-Jones_potential.pdf", dpi=300)
plt.show()
###################################################

a0 = 1.0
na = 4
R = np.array([[(i - 1.5)*a0, 0.0, 0.0] for i in range(na)])
R0 = np.copy(R)
print("R=", R)
print("d=", LA.norm(R[0, :] - R[na-1, :]))


def Etot(n, C):
    s = 0.0
    for i in np.arange(0, n-1):
        # print("i =", i)
        for j in np.arange(i+1, n):
            d = LA.norm(C[i] - C[j])
            s += U(d)
            # print("j =", j, "  s =", s)
    return s


def E_1D(xx):
    if len(xx) != na:
        print("ERROR1")
        exit()
    for i in np.arange(na):
        R[i, 0] = xx[i]
    return Etot(na, R)

xx0 = np.array([R0[i, 0] for i in range(na)])
print("xx0=", xx0)
print("xx0=", tuple(xx0))

xtol = 1.0e-5 # Абсолютная ошибка в оптимизированных аргументах в минимуме
ftol = 1.0e-5
# Находим минимум функции
"""
res1 = fmin(E_1D, xx0, xtol=xtol, ftol=ftol)
print("res1=", res1)
print("res1[1]-res1[0]=", res1[1]-res1[0])
print("res1[2]-res1[1]=", res1[2]-res1[1])
print("res1[3]-res1[2]=", res1[3]-res1[2])
"""
res2 = minimize(E_1D, xx0, method='Nelder-Mead', options={'xtol': xtol, 'disp': False})
print("res2=", res2)
print(dir(res2))
print("res2.fun: ", res2.fun)
print("res2.x  : ", res2.x)
