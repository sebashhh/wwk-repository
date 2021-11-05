# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:46:27 2017

@author: jgerard
"""

#------IMPORT-------#

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(7.0, 4.0))

q_chem_functionals = ['','B3PW91','BMK','CAM-B3LYP','HSE-HJS','LDA','MN15', 'MPW1PW91', 'PBE', '']

functionals = q_chem_functionals

q_chem_excitation_la = [None, 4.9586, 5.2497, 5.1591, 5.0022, 4.5785, 5.1187, 5.0226, 4.5743, None]

q_chem_emission_la = [None, 4.3497, 4.9239, 4.8135, 4.4130, 4.1295, 4.8422, 4.4518, 3.9132, None]

q_chem_excitation_lb = [None, 4.9586, 5.2497, 5.1591, 5.0022, 4.5785, 5.1187, 5.0226, 4.5743, None]

q_chem_emission_lb = [None, 4.7701, 4.8539, 4.9034, 4.8154, 4.3658, 4.8159, 4.5683, 4.3812, None]

#gas abs
La = q_chem_excitation_la

Lb = q_chem_excitation_lb


x = np.arange(0,len(functionals))

plt.scatter(x, La, c='lightcoral', s=200, label="$L_{a}$", zorder=2)
plt.scatter(x, Lb, c='mediumspringgreen', s=200, label="$L_{b}$", zorder=3)

for i in x:
    plt.plot([i, i], [La[i], Lb[i]], 'k-', lw=1, ls='dotted', zorder=1)
   
legend = plt.legend(loc='upper right', shadow=False, fontsize='large', scatterpoints=1)
plt.ylabel("$E$ / eV")
plt.xlim([0,len(functionals)-1])
plt.xticks(x,functionals,rotation=65)



plt.title("Vertical Excitation Energies in Gas Phase")
plt.yticks(np.arange(4, 5.6, 0.5))
plt.ylim([3.5,5.8])

plt.tick_params(top="off")
plt.tick_params(right="off")
plt.show()



fig.savefig('Excitation_Energies.pdf', bbox_inches=None, pad_inches=0, format='pdf', dpi=1200)
