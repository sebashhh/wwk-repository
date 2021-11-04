# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:46:27 2017

@author: jgerard
"""

#------IMPORT-------#

import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(7.0, 4.0))
functionals = ['','CIS','LSDA','BVP86','B3LYP-D','B3PW91','LC-BLYP','LC-PBEPBE','HSEH1PBE','mPW1PW91',
               '$\omega$B97X','APFD','PBE1PBE','MN15','$\omega$B97XD','BH&HLYP','CAM-B3LYP','BMK','M062X','M06','']

#gas abs
La = [None,5.0703,3.8250,3.7413,4,4.1984,4.7390,4.8256,4.2537,
      4.2837,4.6176,4.2476,4.2848,4.3964,4.5017,4.5686,4.4862,4.4478,4.4971,4.6833, None]

Lb = [None,5.1038,4.4951,4.3821,4,4.6961,4.9435,5.0218,4.7463,
      4.7563,4.8241,4.7317,4.7619,4.3967,4.5013,4.5662,4.4850,4.4460,4.4964,4.6755, None]


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
