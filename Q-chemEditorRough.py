# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:58:54 2021

@author: scaparas
"""
import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.log"
fileChoices = []
fileCounter = 0

print(".log files present in directory:")

for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (str(fileCounter) + ": " + entry)
            fileCounter += 1
            fileChoices.append(entry)
print()
print("Type the number index of the Q-Chem file to delete 'au' from it.")
fileIndex = int(input())

with open(fileChoices[fileIndex], 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('au', '  ')

# Write the file out again
with open('Edited' + fileChoices[fileIndex], 'w') as file:
  file.write(filedata)