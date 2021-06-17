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

class logFileData:
    file_name = ""
    mae = ""
    oscillator_strength = 0
    dipole_moment = 0
    mo_transition = []
    root = 0
    
    def __init__(self, file_name):
        self._file_name = file_name
        #assuming that the file names are standardized to end in 1st
        self._root = file_name[-7]
    
    def get_mae(self):
        return self._mae
     
    def set_mae(self, x):
        self._mae = x
    
    def get_oscillator_strength(self):
        return self._oscillator_strength
    
    def set_oscillator_strength(self, x):
        self._oscillator_strength = x
    
    def get_dipole_moment(self):
        return self._dipole_moment
    
    def set_dipole_moment(self, x):
        self.dipole_moment = x
    
    def get_mo_transition(self):
        return self._mo_transition
    
    def append_to_mo_transition(self, x):
        self._mo_transition.append(x)
    
    def get_file_name(self):
        return self._file_name
    
    def get_root(self):
        return self._root

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
def tint(string_to_insert, color):
    tinted_string = f"{color}{string_to_insert}{bcolors.ENDC}".format(
            color = color, string_to_insert = string_to_insert)
    return tinted_string


maeVersus= []
osciVersus= []
dipoleVersus= []
tranVersus= []
homo_value= []

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
def to_guissani(logElement):
    file_name = logElement.get_file_name()
    data = cclib.io.ccread(file_name)
    print("There are %i atoms and %i MOs" % (data.natom, data.nmo) + " in " + file_name)
    data.atomcoords
    coords1 = data.atomcoords[len(data.atomcoords)-1]
#Automatically finds the bond lengths of the atom
    bond_lengths = []
    def dis_formula(pos1, pos2):
        dist = np.linalg.norm(coords1[pos1] - coords1[pos2])
        bond_lengths.append(dist)

    dis_formula(6, 8)
    dis_formula(8, 7)
    dis_formula(7, 4)
    dis_formula(4, 5)
    dis_formula(5, 0)
    dis_formula(0, 1)
    dis_formula(1, 2)
    dis_formula(2, 3)
    dis_formula(3, 6)
    dis_formula(3, 4)

#defining the molecule as done with the keys
    molecule = bond_lengths
    molecule=dict(zip(keys,molecule))

#Compare the opitmized structure to the reference structures
    maeLa = compare(molecule, guissaniLa)
    maeLb = compare(molecule, guissaniLb)
    winner = True if maeLa < maeLb else False

    logElement.set_mae(winner)
    #  print("indole opt structure closest to %s (maeLa=%f, maeLb=%f) dipole=%s" % (winner, maeLa, maeLb, dipole))
    #print(data.etoscs)
   
#Records the oscillator strength according to the function
    #print(logElement.get_root())
    #print("line 142")
    the_osci = data.etoscs[int(logElement.get_root())]
    logElement.set_oscillator_strength(the_osci)

#Now look for the last dipole moment in the file 
#(that of the optimum geometry and the state specified by root=)
    #print(data.moments)        
    dipole = np.linalg.norm(data.moments[1])
    logElement.set_dipole_moment(dipole)

#Variables needed to find the largest coefficient for the transitions
    coeff_versus= []
    lgst_coeff = 0
    
#breaks down Excited State Transition List
    mo_transitions_possible = data.etsecs[0]
    print(data.etsecs)
    print("line 153")
    for mo_element in mo_transitions_possible:
        print(mo_element)
        coeff_versus.append(mo_element[2])
    for element in coeff_versus:
        if abs(element) > abs(lgst_coeff):
            lgst_coeff = element
    for mo_element in mo_transitions_possible:
        if mo_element[2] == lgst_coeff:
            

    
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
    homo_value.append(data.homos[0])
    print(data.etdips)

#describes the raw MO transition numbers in relation to HOMO and LUMO
def transition_formatter (state):
    homo = int(homo_value[0])
    state_string = ""
    the_state = int(state)
    if (state >= homo + 1):
        #AKA LUMO
        state_string += "LUMO"
        if (the_state > homo + 1):
            #if the value is greater than the LUMO 
            state_string += "+" + str(the_state - (homo + 1))
    else:
        #it is HOMO or lower
        state_string += "HOMO"
        if (state < homo):
            state_string += "-" + str(homo - the_state)
    return state_string

#runs the program
def prompt_user():
    list_of_files = os.listdir('.')
    pattern = "*.log"
    file_choices = []
    file_counter = 0
    file_counter_2 = 0
    print(tint(".log files present in directory:", 
               bcolors.LIGHT_PURPLE))
    #looks in current directory for all .log files
    for entry in list_of_files:
        if fnmatch.fnmatch(entry, pattern):
            print (tint(str(file_counter), bcolors.LIGHT_CYAN) + ": " + entry, end= " ")
            file_counter += 1
            file_counter_2 += 1
            file_choices.append(entry)
            if (file_counter_2 == 3):
                print()
                file_counter_2 = 0
    
    print(tint("\nType the number index of a optimization .log and ENTER to learn about the indicators.", 
           bcolors.LIGHT_GREEN))
    print(tint("Type 'done' when complete.", 
           bcolors.LIGHT_GREEN))
    print(tint("Note: You should probably look at fewer files than the number of nstates.", 
           bcolors.DARK_GRAY))
    #log files should be accessible throughout the program
    global log_files
    log_files = [] 
    the_input = ""
    is_inputting = True
    while (is_inputting):    
        the_input = input()
        if (the_input == "done"):
            is_inputting = False
            print(tint("Input done.", 
                       bcolors.LIGHT_GREEN))
        else:
            the_input = int(the_input)
            print("Selected: " + file_choices[the_input] + "\n")
            log_instance = logFileData(file_choices[the_input])
            log_files.append(log_instance)
                  
    for element in log_files:
        to_guissani(element)

prompt_user()
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
            
#def OsciShows (theList):
   #if theList[0] > theList[3]:
        #osciInd.append(tint("La", bcolors.YELLOW))
        #osciInd.append(tint("Lb", bcolors.CYAN))
   #else:
        #osciInd.append(tint("Lb", bcolors.CYAN))
        #osciInd.append(tint("La", bcolors.YELLOW))

def DipoleShows (theList):
     if theList[0] > theList[1]:
        dipoleInd.append(tint("La", bcolors.YELLOW))
        dipoleInd.append(tint("Lb", bcolors.CYAN))

     else:
        dipoleInd.append(tint("Lb", bcolors.CYAN))
        dipoleInd.append(tint("La", bcolors.YELLOW))

 #def TranShows (theList):
   # if theList[0] == homoValue[0] and theList[1] == homoValue[0] + 1:
    #    tranInd.append(tint("La", bcolors.YELLOW))
  #  elif theList[0] == homoValue[0] - 1 and theList[1] == homoValue[0] + 1:
   #     tranInd.append(tint("Lb", bcolors.CYAN))
  #  else:
    #    tranInd.append(tint("N/A", bcolors.DARK_GRAY))
  #  if theList[2] == homoValue[0] and theList[3] == homoValue[0] + 1:
   #     tranInd.append(tint("La", bcolors.YELLOW))
  #  elif theList[2] == homoValue[0] - 1 and theList[3] == homoValue[0] + 1:
   #     tranInd.append(tint("Lb", bcolors.CYAN))
  #  else:
   #     tranInd.append(tint("N/A", bcolors.DARK_GRAY))
        
#runs the functions that append to lists
#MaeShows(maeVersus)
#OsciShows(osciVersus)
#DipoleShows(dipoleVersus)
#TranShows(tranVersus)
    
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



tranPrintedResult = ""
tranPrintedResult += (es1 + "'s MO transition is closest to " + tranInd[0] + " \n"
+ es2 + "'s MO transition is closest to " + tranInd[1] + "\n"
+ es1 + "'s MO transition: " + transition_formatter(tranVersus[0]) + 
tint("->", bcolors.LIGHT_RED) + transition_formatter(tranVersus[1]) + "\n"
+ es2 + "'s MO transition: " + transition_formatter(tranVersus[2]) + 
tint("->", bcolors.LIGHT_RED) + transition_formatter(tranVersus[3]) )

   
print(" \nFour indicators suggest the identity of the indole's top two excited states")
print(tint("MAE indicator:", bcolors.LIGHT_PURPLE)) 
print(maePrintedResult)
print(tint("Oscillator Strength indicator:", bcolors.LIGHT_PURPLE)) 
print(osciPrintedResult)
print(tint("Dipole Moment indicator:", bcolors.LIGHT_PURPLE)) 
print(dipolePrintedResult)
print(tint("MO transition indicator:", bcolors.LIGHT_PURPLE)) 
print(tranPrintedResult)
    


