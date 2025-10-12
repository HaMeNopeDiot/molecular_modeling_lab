import numpy as np
import scipy.optimize as opt
from .avogadro_parser import read_file, write_file


def rosenbrock(x): # Function розенброка
    return(1.0 - x[0])**2 + 100.0*(x[1]-x[0]*x[0])**2

n = 2
x0 = np.zeros(n, dtype=float) # Вектор с двумя элементами типа float
x0[0] = 1
x0[0] = 2
xtol = 1.0e-5 # Абсолютная ошибка в отпимизированных аргументах в минимуме
# Находим минимум функции
res1 = opt.minimize(rosenbrock, 
                    x0, 
                    method='Nelder-Mead',
                    options={'xtol':xtol, 'disp': True})
# print(res1)
"""
Результат:
final_simplex: (array([[1.00000132, 1.0000028 ],
[1.00000014, 0.99999997],
[0.99999681, 0.99999355]]), array([4.38559817e-12,
9.00569749e-12, 1.05977059e-11]))
fun: 4.385598172677925e-12
message: 'Optimization terminated successfully.'
nfev: 269 (число оценок функции)
nit: 143 (число итераций)
status: 0
success: True
x: array([1.00000132, 1.0000028 ])
"""
res2 = opt.fmin(rosenbrock, 
                (0.0, 0.0), 
                xtol=1.0e-5,
                ftol=1.0e-5,
                full_output=0)
# print(res2)

import matplotlib.pyplot as plt
# xs = np.linspace(0.3, 1, 10000)
# plt.plot(xs, [0 for x in xs], color="black")
# plt.plot(xs, [u_r(x) for x in xs])
# plt.show()

epsilon = 0.0103
sigma   = 0.3405

def u_r(r) -> float:
    return 4*epsilon * ((sigma/r)**12 - (sigma/r)**6)

def radius(a, b) -> float:
    return abs(a - b)


n_atoms = 10

import random
x_coord = []
for i in range(n_atoms):
    x_coord.append(random.uniform(0, 0.5))
print(f"x coordinates of atoms: {x_coord}")

import math
def u_total(x: list[float]) -> float:
    u_total = 0
    for j in range(len(x)):
        for i in range(j+1, len(x)):
            r = radius(x[i], x[j])
            u = u_r(r)
            u_total += u
            if math.isnan(u_total):
                print(f"I got here at {j} and {i}")
                exit()
    
    return u_total


xtol = 1.0e-5 # Абсолютная ошибка в отпимизированных аргументах в минимуме
# Находим минимум функции
print("+++++++++++++++++++++")
result = opt.minimize(u_total, 
                    x_coord, 
                    method='Nelder-Mead',
                    options={'xtol':xtol, 'disp': True})
print(result)
xs = np.linspace(1, 0, n_atoms)
# plt.plot(xs, [0 for x in xs], color="black")
a = result.x
a.sort()
plt.scatter(a, [0] * len(a), marker="o")
plt.show()
