import numpy as np
import matplotlib.pyplot as plt

thermo = np.loadtxt('thermo.out')
N = 1000
t = thermo[:,0]
energy = thermo[:,1]+thermo[:,2]
#energy = thermo[:,1]
step = np.arange(0,len(t)*N,N)

plt.figure(0)

plt.plot(step, t)
plt.xlabel('step')
plt.ylabel('temperature (K)')
plt.savefig('temperature.png',dpi=300)

plt.figure(1)
plt.plot(step, energy)
plt.xlabel('step')
plt.ylabel('energy (eV)')
plt.savefig('energy.png',dpi=300)
