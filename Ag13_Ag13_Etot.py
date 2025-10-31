"""
Ag13 clusters
Total energy (Ekin + Epot)
na = 26
na1 = 13
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['text.usetex'] = True
mpl.rc('font', family='serif', size=16)

L = open("lis.txt", "w")

# plt.style.use('bmh')
# plt.style.use('grayscale')
plt.style.use('dark_background')  # черный фон

itM = 300

Ekin, Epot = np.loadtxt("Ag13_Ag13.ene", usecols=(0, 1), unpack=True)  # eV
print("len(Ekin) =", len(Ekin), file=L)
Ekin[:] = Ekin[:] * 1.e-3
Epot[:] = Epot[:] * 1.e-3
print("Ekin =", Ekin, file=L)
print("Epot =", Epot, file=L)
Etot = d = np.array([0.0]*itM)
Etot[:] = Ekin[:] + Epot[:]
d[:] = ((Etot[:]-Etot[1])/Etot[1])*100  # %
dmin = d.min()
dmax = d.max
print("dmin =", dmin, file=L)
print("dmax =", dmax, file=L)

Tsteps = np.arange(itM, dtype=int)
T = np.array(Tsteps, dtype=float)
print("Tsteps =", Tsteps, file=L)
print("len(Tsteps) =", len(Tsteps), file=L)

plt.close('all')
plt.figure(figsize=(8.0, 6.0))
plt.plot(T, d, 'r-', lw=4)
plt.xlabel("number of time's step", fontsize=16)
plt.ylabel(r'$((E_{tot}(t)-E_{tot}(t_0))/E_{tot}(t_0)) \times 100$', fontsize=16)
plt.grid(True)
plt.xlim(0.0, itM)
plt.ylim(-3.0, 3.0)

plt.savefig("Etot.pdf", dpi=300)
plt.show()
