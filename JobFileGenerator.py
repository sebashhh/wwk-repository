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
fileData1 = ""
fileData2 = ""
shData1 = ""
shData2 = ""
romanNumeral = ""

#loads the GJF template from the local directory
with open("!GaussianInputJFG.gjf", 'r') as file :
    filedata1 = file.read()
with open("!GaussianInputJFG.gjf", 'r') as file :
    filedata2 = file.read()

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
    
        filedata1 = filedata1.replace('TITLE', title1)
        filedata2 = filedata2.replace('TITLE', title2)
        filedata1 = filedata1.replace('ROOT', 'root=1')
        filedata2 = filedata2.replace('ROOT', 'root=2')
        filedata1 = filedata1.replace('FUNCTIONAL', functional)
        filedata2 = filedata2.replace('FUNCTIONAL', functional)
        filedata1 = filedata1.replace('BASIS_SET', basisSet)
        filedata2 = filedata2.replace('BASIS_SET', basisSet)

        #Creates root1.gjf
        with open(title1 + ".gjf", 'w') as file:
            file.write(filedata1)
        #Creates root2.gjf    
        with open(title2 + ".gjf", 'w') as file:
            file.write(filedata2)
        isConfiguring = False
    else:
        print("So...you're not ready.")

#TODO make a function to edit all the other things optionally

   


