# -*- coding: utf-8 -*-
"""
Parses excitation energies from Gaussian optimization .log files and plots them
"""
import matplotlib.pyplot as plt
import numpy as np
import cclib

filename="FuncsWB97X-V-2nd.log"
data = cclib.io.ccread(filename)
print("There are %i atoms and %i MOs" % (data.natom, data.nmo))

etenergies = data.etenergies
scfenergies = data.scfenergies
steps = len(scfenergies)
nstates = 6   #adjust to whatever the value of nstates is in your gaussian job

lst=np.array_split(etenergies,steps)
state1 = list(np.array(lst).T[0])
state2 = list(np.array(lst).T[1])


x = np.arange(start=1,stop=steps+1,step=1)

print(x)
print(state1)
print(state2)


plt.plot(x,state1,label="State 1")
plt.plot(x,state2,label="State 2")
plt.xlabel('Optimization Step')
plt.ylabel('Excitation energy/wavenumbers')
plt.legend()
