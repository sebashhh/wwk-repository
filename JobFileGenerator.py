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
basisSet = "6-31+G*"
title1 = "Funcs"
title2 = "Funcs"
title3 = "Funcs"
fileData1 = ""
fileData2 = ""
fileData3 = ""
shData1 = ""
shData2 = ""
shData3 = ""
romanNumeral = ""

#loads the GJF template from the local directory
with open("!GaussianInputJFG.gjf", 'r') as file :
    fileData1 = file.read()
with open("!GaussianInputJFG.gjf", 'r') as file :
    fileData2 = file.read()
with open("!GaussianInputJFG.gjf", 'r') as file :
    fileData3 = file.read()
#loads the gaussian.sh job submission template from the local directory
with open("!gaussianJob.sh", 'r') as file2 :
    shData1 = file2.read()
with open("!gaussianJob.sh", 'r') as file2 :
    shData2 = file2.read()
with open("!gaussianJob.sh", 'r') as file2 :
    shData3 = file2.read()

isConfiguring = True
while isConfiguring:
    print(tint("Default Functional: ", bcolors.CYAN) + functional)
    print(tint("Set Gaussian Functional for testing: \nType 'ok' to proceed with the default.", bcolors.LIGHT_CYAN))
    
    theInput = str(input())
    if(theInput.lower() != "ok"):
        functional = theInput
    print(tint("Default Roman Numeral: ", bcolors.CYAN) + romanNumeral)
    print(tint("Set Roman Numeral to avoid repeat titles. \nType 'ok' to proceed with the default.", bcolors.LIGHT_CYAN))
    
    theInput = str(input())
    if(theInput.lower() != "ok"):
        romanNumeral = theInput.upper()
    
    print(tint("Current Settings: ", bcolors.CYAN))
    print("Functional: " + functional)
    print("Basis Set: " + basisSet)
    print("Roman Numeral: " + romanNumeral)
    
    print(tint("Set Gaussian Functional for testing. \nType 'ok' to generate your .gjf's.", bcolors.LIGHT_CYAN))
    theInput = str(input())
    if(theInput.lower() == "ok"):
        title1 += functional + romanNumeral + "1st"
        title2 += functional + romanNumeral + "2nd"
        title3 += functional + romanNumeral + "3rd"
    
        fileData1 = fileData1.replace('TITLE', title1)
        fileData2 = fileData2.replace('TITLE', title2)
        fileData3 = fileData3.replace('TITLE', title3)
        
        fileData1 = fileData1.replace('ROOT', 'root=1')
        fileData2 = fileData2.replace('ROOT', 'root=2')
        fileData3 = fileData3.replace('ROOT', 'root=3')
        
        fileData1 = fileData1.replace('FUNCTIONAL', functional)
        fileData2 = fileData2.replace('FUNCTIONAL', functional)
        fileData3 = fileData3.replace('FUNCTIONAL', functional)
        
        fileData1 = fileData1.replace('BASIS_SET', basisSet)
        fileData2 = fileData2.replace('BASIS_SET', basisSet)
        fileData3 = fileData3.replace('BASIS_SET', basisSet)
        
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

   


