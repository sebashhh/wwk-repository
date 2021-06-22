# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:58:54 2021

@author: scaparas
"""

class bcolors:
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
#tint colors a String inserted. It is more readable and can be autocompleted with Shift+Space.
def tint(stringToInsert, color):
    tintedString = f"{color}{stringToInsert}{bcolors.ENDC}".format(
            color = color, stringToInsert = stringToInsert)
    return tintedString

functional = ""
basis_set = "6-31+G*"
titles = []
file_data = []
sh_data = []
roman_numeral = ""

#loads the GJF template from the local directory
for i in range(2)
    with open("!QChemInput.in", 'r') as file :
        file_data[i] = file.read()
#loads the qchem.in job submission template from the local directory
    with open("!qchemJob.sh", 'r') as file_2 :
        sh_data[i] = file_2.read()

#prompts the user to configure their settings
is_configuring = True
while is_configuring:
    print(tint("Default Functional: ", 
               bcolors.CYAN) + functional)
    print(tint("Set Q-Chem Functional for testing: "
               + "\nType 'ok' to proceed with the default.", 
               bcolors.LIGHT_CYAN))
    
    the_input = str(input())
    if(the_input.lower() != "ok"):
        functional = the_input
    print(tint("Default Roman Numeral: ", 
               bcolors.CYAN) + roman_numeral)
    print(tint("Set Roman Numeral to avoid repeat titles. " + 
               "\nType 'ok' to proceed with the default.", 
               bcolors.LIGHT_CYAN))
    
    the_input = str(input())
    if(the_input.lower() != "ok"):
        romanNumeral = the_input.upper()
    
    print(tint("Current Settings: ", 
               bcolors.CYAN))
    print("Functional: " + functional)
    print("Basis Set: " + basis_set)
    print("Roman Numeral: " + roman_numeral)
    
    print(tint("Set Q-Chem Functional for testing." +
               "\nType 'ok' to generate your .gjf's.", 
               bcolors.LIGHT_CYAN))
    the_input = str(input())
    if(the_input.lower() == "ok"):
        for i in range(2)
            titles[i] = "Qfuncs"
            titles[i] += functional + "-" + romanNumeral + "-"
            
            if (i == 0):
                titles[i] += "1st"
                elif (i == 1):
                    titles[i] += "2nd"
                    elif (i == 2):
                        titles[i] += "3rd"
            
        
            file_data[i] = file_data[i].replace(
                'TITLE', titles[i])
        
        fileData1 = fileData1.replace('ROOT', 'root=1')
        fileData2 = fileData2.replace('ROOT', 'root=2')
        fileData3 = fileData3.replace('ROOT', 'root=3')
        
        fileData1 = fileData1.replace('FUNCTIONAL', functional)
        fileData2 = fileData2.replace('FUNCTIONAL', functional)
        fileData3 = fileData3.replace('FUNCTIONAL', functional)
        
        fileData1 = fileData1.replace('BASIS_SET', basis_set)
        fileData2 = fileData2.replace('BASIS_SET', basis_set)
        fileData3 = fileData3.replace('BASIS_SET', basis_set)
        
        shData1 = shData1.replace('TITLE', title1)
        shData2 = shData2.replace('TITLE', title2)
        shData3 = shData3.replace('TITLE', title3)
        #Creates root1.gjf
        with open(title1 + ".gjf", 'w') as file:
            file.write(fileData1)
        #Creates root2.gjf    
        with open(title2 + ".gjf", 'w') as file:
            file.write(fileData2)
        #Creates root3.gjf
        with open(title3 + ".gjf", 'w') as file:
            file.write(fileData3)
        #Creates root1.sh
        with open(title1 + ".sh", 'w') as file2:
            file2.write(shData1)
        #Creates root2.sh    
        with open(title2 + ".sh", 'w') as file2:
            file2.write(shData2)
        #Creates root3.sh  
        with open(title3 + ".sh", 'w') as file2:
            file2.write(shData3)
        isConfiguring = False
    else:
        print("So...you're not ready.")

#TODO make a function to edit all the other things optionally

   


