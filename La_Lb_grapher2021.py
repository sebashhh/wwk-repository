# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:46:27 2017

@author: jgerard
"""

#------IMPORT-------#

import numpy as np
import matplotlib.pyplot as plt
import StringTinter as t
import GiussaniVersus2021 as gv

plot_width = 7.0
plot_height = 4.0
#sets bounds of plot
fig = plt.figure(figsize=(plot_width, plot_height))

#list of functionals in use (x, independent variable)
functionals = ['']

La_Lb_grapher_prompt = (
    (t.tint("\nType the La file, then the Lb for each functional you want to plot." +
            "\nType 'done' when complete.", 
           t.bcolors.LIGHT_GREEN)) 
    ) 
print("here")
gv.log_file_select(La_Lb_grapher_prompt)
the_count = 0
for element in gv.log_files:
    the_count = the_count + 1
    gv.to_guissani(element)
    #print(element.get_file_name())
    #pulls the functional from what ought to be the root 1 entry
    if (the_count % 2) == 1:
        functionals.append(element.get_functional())
functionals.append('')
    
print(functionals)

#Vertical Excitation Energies in Gas Phase? (y, dependent variable)
La = [None,5.0703,3.8250,3.7413,4,4.1984,
      4.7390,4.8256,4.2537,4.2837,4.6176,
      4.2476,4.2848,4.3964,4.5017,4.5686,4.4862,4.4478,4.4971,4.6833, None]
Lb = [None,5.1038,4.4951,4.3821,4,4.6961,
      4.9435,5.0218,4.7463,4.7563,4.8241,
      4.7317,4.7619,4.3967,4.5013,4.5662,4.4850,4.4460,4.4964,4.6755, None]


x = np.arange(0,len(functionals))

#scatter()
#x,y
#s=marker size
#c=color
#label=label
#zorder=front to back order, higher numbers go frontward
plt.scatter(x, La, s=200, c='lightcoral', label="$L_{a}$", zorder=2)
plt.scatter(x, Lb, s=200, c='mediumspringgreen', label="$L_{b}$", zorder=3)

for i in x:
    plt.plot([i, i], [La[i], Lb[i]], 'k-', lw=1, ls='dotted', zorder=1)

#creates a legend box
legend = plt.legend(loc='upper right', shadow=False, fontsize='large', scatterpoints=1)
#labels the y axis
plt.ylabel("$E$ / eV")
#creates hashes on the x-axis
plt.xlim([0,len(functionals)-1])
plt.xticks(x,functionals,rotation=65)

#titles the plot
plt.title("Vertical Excitation Energies in Gas Phase")
plt.yticks(np.arange(4, 5.6, 0.5))
plt.ylim([3.5,5.8])

plt.tick_params(top="off")
plt.tick_params(right="off")
plt.show()


fig.savefig('Excitation_Energies.pdf', bbox_inches=None, pad_inches=0, format='pdf', dpi=1200)
