
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
import math

#a class that store the indicators of La/Lb states as attributes
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
    _dmv_angle = 0
    _dmv_quadrant = "Phantom"
    
    def __init__(self, file_name):
        self._file_name = file_name
        #assuming that the file names are standardized to end in 1st
        self._root = file_name[-7]
    
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
        return int(self._root)
    
    def get_formatted_mo(self):
        return self._formatted_mo
    
    def set_formatted_mo(self, x):
        self._formatted_mo = x
        
    def get_homo(self):
        return self._homo
    
    def set_homo(self, x):
        self._homo = x
    
    def get_dmv_angle(self):
        return self._dmv_angle
    
    def set_dmv_angle(self, x):
        self._dmv_angle = x
    
    def get_dmv_quadrant(self):
        return self._dmv_quadrant
   
    def set_dmv_quadrant(self, x):
        self._dmv_quadrant = x

#ANSI escape code colors
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

#we may observe the dmv direction osc9346illating between quadrants, 
#but keeping the same angle  
#vertical angles are always congruent

#the quadrants of dipole moment vector (dmv) direction
class quadrants:
    #Lb
    ONE = "-,+"
    #La
    TWO = "+,+"
    #Lb
    THREE = "+,-"
    #La
    FOUR = "-,-"

# simple function to compare one molecule to another and calculate sum of the absolute errors
def compare(mol1, mol2):
    mae = 0.0
    for (key1, val1), (key2, val2) in zip(mol1.items(), mol2.items()):
        mae += abs(val1-val2)
    #print "comparison made! mae = %f" % mae
    return mae

#Defining the built in structures for this script, particularly the reference structures from the 2011 Guissani paper
keys = ['r45', 'r56', 'r16', 'r12', 'r23', 'r34', 'r17', 'r78', 'r816', 'r216']
guissani_GS = [ 1.376,  1.363,  1.441, 1.405, 1.384, 1.411, 1.385,  1.400,  1.372, 1.404]
guissani_La = [ 1.314,  1.445, 1.436, 1.412, 1.426,  1.377,  1.447,  1.391,  1.407, 1.403]
guissani_Lb = [ 1.403, 1.385, 1.420, 1.419, 1.430, 1.446, 1.431, 1.404, 1.367, 1.466]
zero = [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 0.]

#Now officially make the molecular structures, stored as python dictionaries using the bond labels as keys
guissani_GS = dict(zip(keys,guissani_GS))
guissani_La = dict(zip(keys,guissani_La))
guissani_Lb = dict(zip(keys,guissani_Lb))
zero = dict(zip(keys,zero))

#Parses out the indicators for each 
def to_guissani(logElement):
    file_name = logElement.get_file_name()
    data = cclib.io.ccread(file_name)
    print("There are %i atoms and %i MOs" % (data.natom, data.nmo) + " in " + file_name)
    data.atomcoords
    coords1 = data.atomcoords[len(data.atomcoords)-1]
    #Automatically finds the bond lengths of the atom
    bond_lengths = []
    #if you want to just see the data.<attribute> of something quickly, put it between
    #~here~
    
    #print(data.etdips)
    #print(data.etdips[0])
    #print(data.etdips[0][0])
    
    #~and here~
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
        print(tint(("no oscillator strength found for root: " + str(logElement.get_root())), 
              bcolors.DARK_GRAY))
             
    #Now look for the last dipole moment in the file 
    #(that of the optimum geometry and the state specified by root=)     
    dipole = np.linalg.norm(data.moments[1])
    logElement.set_dipole_moment(dipole)

    #Variables needed to find the largest coefficient for the transitions
    coeff_versus= []
    lgst_coeff = 0
    
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
         print(tint(("no MO transition found for root: " + str(logElement.get_root())), 
                    bcolors.DARK_GRAY))
    try: 
        #e.g. the first root would pull from the first excited state
        dmv = data.etdips[logElement.get_root() - 1]
        #TODO: if it's necessary, maybe it's better to preserve the negatives for the calculations
        x_vector = dmv[0]
        y_vector = dmv[1]
        z_vector = dmv[2]
        if (x_vector < 0):
        #(-, ?)
            if (y_vector < 0):
                logElement.set_dmv_quadrant(quadrants.FOUR)
            else:
                logElement.set_dmv_quadrant(quadrants.ONE)
        else:
        #(+, ?)
            if (y_vector < 0):
                logElement.set_dmv_quadrant(quadrants.THREE)
            else:
                logElement.set_dmv_quadrant(quadrants.TWO)
        dot_product = abs(x_vector * 1) + abs(y_vector * 0)
        vector_magnitude = math.sqrt((x_vector**2) + (y_vector**2)) * math.sqrt((1**2) + (0**2))
        theta = math.acos(dot_product/vector_magnitude)
        logElement.set_dmv_angle(radian_to_degrees(theta))
    except IndexError:
         print(tint(("no dipole moment vector found for root: " + str(logElement.get_root())), 
                    bcolors.DARK_GRAY))

#describes the raw MO transition numbers in relation to HOMO and LUMO
def transition_formatter (logElement, state):
    homo = int(logElement.get_homo())
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

#converts radians to degrees 
def radian_to_degrees(radian_value):
    ratio = (180/(math.pi))
    degree_value = radian_value * ratio
    return degree_value

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
            print("Selected: " + file_choices[the_input])
            #constructor call
            log_instance = logFileData(file_choices[the_input])
            log_files.append(log_instance)
                  
    for element in log_files:
        to_guissani(element)

#prints out info on each indicator
def print_out_info():
    es = "Energy State" 
    print(" \nFour indicators suggest the identity of the indole's top two excited states")
    print(tint("MAE indicator:", 
               bcolors.LIGHT_PURPLE)) 
    for element in log_files:
        mae_printed_result = (es + " " + str(element.get_root()) + "'s structure is closest to " 
                              + element.get_mae() + ". " + "maeLa: " + element.get_mae_La() 
        + " maeLb: " + element.get_mae_Lb())
        print(mae_printed_result)
    print(tint("Oscillator Strength indicator:", 
               bcolors.LIGHT_PURPLE)) 
    for element in log_files:
        osci_printed_result = (es + " " + str(element.get_root()) + "'s oscillator strength: " 
                             + str(element.get_oscillator_strength()))
        print(osci_printed_result)
    print(tint("Dipole Moment indicator:", 
               bcolors.LIGHT_PURPLE))
    for element in log_files:
        dipole_printed_result = (es + " " + str(element.get_root()) + "'s dipole moment: " 
                               + str(element.get_dipole_moment()))
        print(dipole_printed_result)
    print(tint("MO transition indicator:", 
               bcolors.LIGHT_PURPLE)) 
    for element in log_files:
        tran_printed_result = (es + " " + str(element.get_root()) + "'s MO transition is closest to " 
                             + element.get_formatted_mo())
        print(tran_printed_result)
    print(tint("Dipole Moment Vector indicator:", 
               bcolors.LIGHT_PURPLE))
    for element in log_files:
        dmv_printed_result= (es + " " + str(element.get_root()) + "'s Dipole Moment Vector is: " 
                             + str(element.get_dmv_angle()) + " degrees")
        dmv_printed_result += ("\nThe vectors point: " + element.get_dmv_quadrant() + ", indicative of the ")
        if (element.get_dmv_quadrant() == quadrants.TWO or element.get_dmv_quadrant() == quadrants.FOUR ):
            dmv_printed_result += "La excited state"
        elif (element.get_dmv_quadrant() == quadrants.ONE or element.get_dmv_quadrant() == quadrants.THREE):
            dmv_printed_result += "Lb excited state"
        print(dmv_printed_result)
#actual method calls
prompt_user()
print_out_info()


    


