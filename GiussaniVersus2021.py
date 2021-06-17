# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:49:06 2020

@author: Capar
"""
#Formatted comparison of two roots
#Possible future version could quantitatively say when values are too close to discern which way or the other
import cclib
import numpy as np
import os, fnmatch
#import sys

<<<<<<< HEAD
#if not sys.warnoptions:
    #import warnings
    #warnings.simplefilter("ignore") # Change the filter in this process
=======
class logFileData:
    _file_name = ""
    _mae = ""
    _oscillator_strength = 0
    _dipole_moment = 0
    _mo = []
    _formatted_mo = "N/A"
    _root = 0
    _homo = 0
    _mae_La = ""
    _mae_Lb = ""
>>>>>>> 3ce0acc (functional for 1, 2, and 3)
    
    
<<<<<<< HEAD
=======
    def get_mae(self):
        return self._mae
     
    def set_mae(self, x):
        self._mae = str(x)
    
    def get_mae_La(self):
        return self._mae_La
     
    def set_mae_La(self, x):
        self._mae_La = str(x)
    
    def get_mae_Lb(self):
        return self._mae_Lb
     
    def set_mae_Lb(self, x):
        self._mae_Lb = str(x)
    
    def get_oscillator_strength(self):
        return self._oscillator_strength
    
    def set_oscillator_strength(self, x):
        self._oscillator_strength = str(x)
    
    def get_dipole_moment(self):
        return self._dipole_moment
    
    def set_dipole_moment(self, x):
        self._dipole_moment = str(x)
    
    def get_mo(self):
        return self._mo
    
    def append_to_mo(self, x):
        self._mo.append(x)
    
    def get_file_name(self):
        return self._file_name
    
    def get_root(self):
        return self._root
    
    def get_formatted_mo(self):
        return self._formatted_mo
    
    def set_formatted_mo(self, x):
        self._formatted_mo = x
        
    def get_homo(self):
        return self._homo
    
    def set_homo(self, x):
        self._homo = x

>>>>>>> 3ce0acc (functional for 1, 2, and 3)
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

listOfFiles = os.listdir('.')
pattern = "*.log"
fileChoices = []
fileCounter = 0
print(tint(".log files present in directory:", bcolors.LIGHT_PURPLE))

<<<<<<< HEAD
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (tint(str(fileCounter), bcolors.LIGHT_CYAN) + ": " + entry)
            fileCounter += 1
            fileChoices.append(entry)
print()
maeVersus= []
osciVersus= []
dipoleVersus= []
tranVersus= []
homoValue= []

=======
>>>>>>> 3ce0acc (functional for 1, 2, and 3)
# simple function to compare one molecule to another and calculate sum of the absolute errors
def compare(mol1, mol2):
    mae = 0.0
    for (key1, val1), (key2, val2) in zip(mol1.items(), mol2.items()):
        mae += abs(val1-val2)
    #print "comparison made! mae = %f" % mae
    return mae

#Defining the built in structures for this script, particularly the reference structures from the 2011 Guissani paper
keys = ['r45', 'r56', 'r16', 'r12', 'r23', 'r34', 'r17', 'r78', 'r816', 'r216']
guissaniGS = [ 1.376,  1.363,  1.441, 1.405, 1.384, 1.411, 1.385,  1.400,  1.372, 1.404]
guissaniLa = [ 1.314,  1.445, 1.436, 1.412, 1.426,  1.377,  1.447,  1.391,  1.407, 1.403]
guissaniLb = [ 1.403, 1.385, 1.420, 1.419, 1.430, 1.446, 1.431, 1.404, 1.367, 1.466]
zero = [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.]

#Now officially make the molecular structures, stored as python dictionaries using the bond labels as keys
guissaniGS = dict(zip(keys,guissaniGS))
guissaniLa = dict(zip(keys,guissaniLa))
guissaniLb = dict(zip(keys,guissaniLb))
zero = dict(zip(keys,zero))

#Prints Atoms, MOs, Bond Lengths, MAE, ESTs, the HOMO, Oscillator Strength
def ToGuissani(theName):
    filename=theName
    data = cclib.io.ccread(filename)
    print("There are %i atoms and %i MOs" % (data.natom, data.nmo) + " in " + filename)
    data.atomcoords
    coords1= data.atomcoords[len(data.atomcoords)-1]
#Automatically finds the bond lengths of the atom
    bondLeng= []
    def disFormula(pos1, pos2):
        dist = np.linalg.norm(coords1[pos1] - coords1[pos2])
        bondLeng.append(dist)

    disFormula(6, 8)
    disFormula(8, 7)
    disFormula(7, 4)
    disFormula(4, 5)
    disFormula(5, 0)
    disFormula(0, 1)
    disFormula(1, 2)
    disFormula(2, 3)
    disFormula(3, 6)
    disFormula(3, 4)

#defining the molecule as done with the keys
    molecule = bondLeng
    molecule=dict(zip(keys,molecule))

<<<<<<< HEAD
#Compare the opitmized structure to the reference structures
    maeLa = compare(molecule, guissaniLa)
    maeLb = compare(molecule, guissaniLb)
    winner = True if maeLa < maeLb else False

    maeVersus.append(winner)
    #  print("indole opt structure closest to %s (maeLa=%f, maeLb=%f) dipole=%s" % (winner, maeLa, maeLb, dipole))
=======
    #Compare the opitmized structure to the reference structures
    mae_La = compare(molecule, guissani_La)
    mae_Lb = compare(molecule, guissani_Lb)
    winner = True if mae_La < mae_Lb else False
    the_mae = ""
    if (winner == True):
        the_mae = "La"
    else:
        the_mae = "Lb"
    logElement.set_mae(the_mae)
    logElement.set_mae_La(mae_La)
    logElement.set_mae_Lb(mae_Lb)
    try:
        the_osci = data.etoscs[int(logElement.get_root())]
        logElement.set_oscillator_strength(the_osci)
    except IndexError:
        print(tint(("no oscillator strength found for root: " + logElement.get_root()), 
              bcolors.DARK_GRAY))
              
>>>>>>> 3ce0acc (functional for 1, 2, and 3)

#Appends the Oscillator Strength List
    lastOscis=data.etoscs[-(6):-1]
  #  print(data.etsecs[0][0])
#Oscillator strength, excited state 1
    osciVersus.append(lastOscis[0])
#Oscillator strength, excited state 2
    osciVersus.append(lastOscis[1])

#Now look for the last dipole moment in the file (that of the optimum geometry and the state specified by root=)
    dipole = np.linalg.norm(data.moments[1])

#And send it to Versus for Comparison
    dipoleVersus.append(dipole)

#breaks down Excited State Transition List
    lastEtsecs=[data.etsecs[-(6):-1]]
    
#populates the tranVersus list by fetching finding the highest coefficient
    coeffVersus= []
    lgstCoeff = 0
    
    #if toGiussani has already been called on the first file
    if (len(tranVersus) == 2):
        #for each guess at the transition in the first row
        for i in lastEtsecs[0][1]:
            #append the coefficient
            coeffVersus.append(i[2])
        for element in coeffVersus:
            if abs(element) > abs(lgstCoeff):
                lgstCoeff = element
        for j in lastEtsecs[0][1]:
            if j[2] == lgstCoeff:
                tranVersus.append(j[0][0])
                tranVersus.append(j[1][0])
    else:
        #for each guess at the transition in the first row
        for i in lastEtsecs[0][0]:
            #append the coefficient
            coeffVersus.append(i[2])
    #search for the highest

        for element in coeffVersus:
            if abs(element) > abs(lgstCoeff):
                
                lgstCoeff = element
    #append the transition associated with the highest coefficient
        for j in lastEtsecs[0][0]:
            if j[2] == lgstCoeff:
                
                tranVersus.append(j[0][0])
                tranVersus.append(j[1][0])
            
#finds the HOMO and stores it in HOMO value
    homoValue.append(data.homos[0])
    
<<<<<<< HEAD
    #print transition dipole moment
    print(data.etdips)
#runs the program
print(tint("Type the number index of two optimization .log files to compare.", bcolors.LIGHT_GREEN))
fileOne = int(input())
print("Selected: " + fileChoices[fileOne]) 
fileTwo = int(input())
print("Selected: " + fileChoices[fileTwo] + "\n")

ToGuissani(fileChoices[fileOne])
ToGuissani(fileChoices[fileTwo])

maeInd = []
osciInd = []
dipoleInd = []
tranInd = []

def MaeShows (theList):
    for k in theList:
        if k == True:
            maeInd.append(tint("La", bcolors.YELLOW)) 
        else:
            maeInd.append(tint("Lb", bcolors.CYAN))
            
def OsciShows (theList):
   if theList[0] > theList[3]:
        osciInd.append(tint("La", bcolors.YELLOW))
        osciInd.append(tint("Lb", bcolors.CYAN))
   else:
        osciInd.append(tint("Lb", bcolors.CYAN))
        osciInd.append(tint("La", bcolors.YELLOW))

def DipoleShows (theList):
     if theList[0] > theList[1]:
        dipoleInd.append(tint("La", bcolors.YELLOW))
        dipoleInd.append(tint("Lb", bcolors.CYAN))

     else:
        dipoleInd.append(tint("Lb", bcolors.CYAN))
        dipoleInd.append(tint("La", bcolors.YELLOW))

def TranShows (theList):
    if theList[0] == homoValue[0] and theList[1] == homoValue[0] + 1:
        tranInd.append(tint("La", bcolors.YELLOW))
    elif theList[0] == homoValue[0] - 1 and theList[1] == homoValue[0] + 1:
        tranInd.append(tint("Lb", bcolors.CYAN))
    else:
        tranInd.append(tint("N/A", bcolors.DARK_GRAY))
    if theList[2] == homoValue[0] and theList[3] == homoValue[0] + 1:
        tranInd.append(tint("La", bcolors.YELLOW))
    elif theList[2] == homoValue[0] - 1 and theList[3] == homoValue[0] + 1:
        tranInd.append(tint("Lb", bcolors.CYAN))
    else:
        tranInd.append(tint("N/A", bcolors.DARK_GRAY))
        
#runs the functions that append to lists
MaeShows(maeVersus)
OsciShows(osciVersus)
DipoleShows(dipoleVersus)
TranShows(tranVersus)
    
es1 = "Energy State 1"
es2 = "Energy State 2"

maePrintedResult = ""
maePrintedResult += (es1 + "'s structure is closest to " + maeInd[0] + " \n" +
es2 + "'s structure is closest to " + maeInd[1])
    
osciPrintedResult = ""
if (abs(osciVersus[0] - osciVersus[3]) < .001):
    osciPrintedResult += "Oscillator Strengths are too close. Optimization likely confused. \n"
else: 
    osciPrintedResult += (es1 + "'s oscillator strength is closest to " + osciInd[0] + " \n"
    + es2 + "'s oscillator strength is closest to " + osciInd[1] + "\n")

osciPrintedResult += (es1 + "'s oscillator strength: " + str(osciVersus[0]) + "\n"
    + es2 + "'s oscillator strength: " + str(osciVersus[3]) )
    
dipolePrintedResult = ""
if (abs(dipoleVersus[0] - dipoleVersus[1]) < .001):
    dipolePrintedResult += "Dipole Moments are too close. Optimization likely confused."
else: 
    dipolePrintedResult += (es1 + "'s dipole moment is closest to " + dipoleInd[0] + " \n"
    + es2 + "'s dipole moment is closest to " + dipoleInd[1] + "\n")

dipolePrintedResult += (es1 + "'s dipole moment: " + str(dipoleVersus[0]) + "\n"
                        + es2 + "'s dipole moment: " + str(dipoleVersus[1]))

def transitionFormatter (state):
    homo = int(homoValue[0])
    stateString = ""
    theState = int(state)
=======
    #finds the homo and sets it
    logElement.set_homo(data.homos[0])
    #breaks down Excited State Transition List
    try: 
        mo_transitions_possible = data.etsecs[0]

        #find the transitions and formats them
        for mo_element in mo_transitions_possible:
            coeff_versus.append(mo_element[2])
        for element in coeff_versus:
            if abs(element) > abs(lgst_coeff):
                lgst_coeff = element
        for mo_element in mo_transitions_possible:
            if mo_element[2] == lgst_coeff:
                logElement.append_to_mo(mo_element[0][0])
                logElement.append_to_mo(mo_element[1][0])

        the_mo = logElement.get_mo()
        logElement.set_formatted_mo(transition_formatter(logElement, the_mo[0]) 
                                    + tint("->", bcolors.LIGHT_RED) 
                                    + transition_formatter(logElement, the_mo[1]))
    except IndexError:
         print(tint(("no MO transition found for root: " + logElement.get_root()), 
                    bcolors.DARK_GRAY))
              
#describes the raw MO transition numbers in relation to HOMO and LUMO
def transition_formatter (logElement, state):
    homo = int(logElement.get_homo())
    state_string = ""
    the_state = int(state)
>>>>>>> 3ce0acc (functional for 1, 2, and 3)
    if (state >= homo + 1):
        #AKA LUMO
        stateString += "LUMO"
        if (state > homo + 1):
            #if the value is greater than the LUMO 
            stateString += "+" + str(theState - (homo + 1))
    else:
        #it is HOMO or lower
        stateString += "HOMO"
        if (state < homo):
            stateString += "-" + str(homo - theState)
    return stateString

tranPrintedResult = ""
tranPrintedResult += (es1 + "'s MO transition is closest to " + tranInd[0] + " \n"
+ es2 + "'s MO transition is closest to " + tranInd[1] + "\n"
+ es1 + "'s MO transition: " + transitionFormatter(tranVersus[0]) + 
tint("->", bcolors.LIGHT_RED) + transitionFormatter(tranVersus[1]) + "\n"
+ es2 + "'s MO transition: " + transitionFormatter(tranVersus[2]) + 
tint("->", bcolors.LIGHT_RED) + transitionFormatter(tranVersus[3]) )
    
print(" \nFour indicators suggest the identity of the indole's top two excited states")
print(tint("MAE indicator:", bcolors.LIGHT_PURPLE)) 
print(maePrintedResult)
print(tint("Oscillator Strength indicator:", bcolors.LIGHT_PURPLE)) 
print(osciPrintedResult)
print(tint("Dipole Moment indicator:", bcolors.LIGHT_PURPLE)) 
print(dipolePrintedResult)
print(tint("MO transition indicator:", bcolors.LIGHT_PURPLE)) 
print(tranPrintedResult)
    


