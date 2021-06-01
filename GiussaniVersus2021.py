# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:49:06 2020

@author: Capar
"""
#Formatted comparison of two roots
#Possible future version could quantitatively say when values are too close to discern which way or the other
import cclib
import numpy as np


maeVersus= []
osciVersus= []
dipoleVersus= []
tranVersus= []
homoValue= []

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
   # print("There are %i atoms and %i MOs" % (data.natom, data.nmo))
  #  print()
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

#Compare the opitmized structure to the reference structures
    maeLa = compare(molecule, guissaniLa)
    maeLb = compare(molecule, guissaniLb)
    winner = True if maeLa < maeLb else False

    maeVersus.append(winner)
    #  print("indole opt structure closest to %s (maeLa=%f, maeLb=%f) dipole=%s" % (winner, maeLa, maeLb, dipole))

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


    for i in lastEtsecs[0][0]:
        coeffVersus.append(i[2])
    for index in coeffVersus:
        if index > lgstCoeff:
            lgstCoeff = index
    for j in lastEtsecs[0][0]:
        if j[2] == lgstCoeff:
            tranVersus.append(j[0][0])
            tranVersus.append(j[1][0])
#finds the HOMO and stores it in HOMO value
    homoValue.append(data.homos[0])

#print(bondLeng)
    print(maeVersus)
    print(osciVersus)
    print(dipoleVersus)
    print(tranVersus)
    print(homoValue)
ToGuissani("indole-tddft-wb97x1.out")
ToGuissani("indole-tddft-wb97x2.out")

maeInd = []
osciInd = []
dipoleInd = []
tranInd = []


def MaeShows (theList):
    for k in theList:
        if k == True:
            maeInd.append("La")
        else:
            maeInd.append("Lb")
def OsciShows (theList):
   if theList[0] > theList[3]:
        osciInd.append("La, Lb")
   else:
        osciInd.append("Lb, La")
def DipoleShows (theList):
     if theList[0] > theList[1]:
        dipoleInd.append("La, Lb")
     else:
        dipoleInd.append("Lb, La")
def TranShows (theList):
#print (theList[1])
#print (homoValue[0] + 1)
    if theList[0] == homoValue[0] and theList[1] == homoValue[0] + 1:
        tranInd.append("La")
    elif theList[0] == homoValue[0] - 1 and theList[1] == homoValue[0] + 1:
        tranInd.append("Lb")
    else:
        tranInd.append("N/A")
    if theList[2] == homoValue[0] and theList[3] == homoValue[0] + 1:
        tranInd.append("La")
    elif theList[2] == homoValue[0] - 1 and theList[3] == homoValue[0] + 1:
        tranInd.append("Lb")
    else:
        tranInd.append("N/A")
MaeShows(maeVersus)
OsciShows(osciVersus)
DipoleShows(dipoleVersus)
TranShows(tranVersus)


print("The four indicators tell us the identity of the indole's top two excited states")
print("Energy State 1, Energy State 2")
print("MAE indictates-- ")
print(maeInd)
print("Osci indictates-- ")
print(osciInd)
print("Dipole indictates-- ")
print(dipoleInd)
print("Tran indictates-- ")
print(tranInd)



