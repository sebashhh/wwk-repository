# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:46:27 2017

@author: jgerard
"""

#------IMPORT-------#

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(7.0, 4.0))

plot_title = "Vertical Emission Energies in Gas Phase"

figure_name = 'Emission_Energies.pdf'

q_chem_functionals = ['','B3PW91','BMK','CAM-B3LYP',
                      'HSE-HJS','LDA','MN15', 'MPW1PW91', 'PBE', '']

functionals = q_chem_functionals

q_chem_excitation_la = [None, 4.9586, 5.2497, 5.2636, 5.0022, 4.7432, 
                        5.1187, 5.0291, 4.5774, 
                        None]

q_chem_emission_la = [None, 4.3497, 4.9239, 4.8754, 4.4130, 4.2273,
                      4.8422, 4.6435, 4.2613,
                      None]

q_chem_excitation_lb = [None, 5.0199, 5.3133, 5.1591, 5.0633, 4.7605, 
                        5.2126, 5.0727, 4.7538,
                        None]

q_chem_emission_lb = [None, 4.7736, 5.0343, 4.9034, 4.8344, 4.5846,
                      4.9261, 4.9847, 4.4659,
                      None]

#gas abs
La = q_chem_emission_la

Lb = q_chem_emission_lb


x = np.arange(0,len(functionals))

plt.scatter(x, La, c='lightcoral', s=200, label="$L_{a}$", zorder=2)
plt.scatter(x, Lb, c='mediumspringgreen', s=200, label="$L_{b}$", zorder=3)

for i in x:
    plt.plot([i, i], [La[i], Lb[i]], 'k-', lw=1, ls='dotted', zorder=1)
   
legend = plt.legend(loc='upper right', shadow=False, fontsize='large', scatterpoints=1)
plt.ylabel("$E$ / eV")
plt.xlim([0,len(functionals)-1])
plt.xticks(x,functionals,rotation=65)



plt.title(plot_title)
plt.yticks(np.arange(4, 5.6, 0.5))
plt.ylim([3.5,5.8])

plt.tick_params(top="off")
plt.tick_params(right="off")
plt.show()



fig.savefig(figure_name, bbox_inches=None, pad_inches=0, format='pdf', dpi=1200)
