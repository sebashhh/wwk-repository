# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 03:08:21 2022
Molecular Dynamics
Adapted from previous Jupyter notebooks
@author: scaparas
"""

#Import Libraries
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
from time import time

#Load a Structure and set up the simulation
salt = PDBFile('nacl.pdb')
forcefield = ForceField('amber14/protein.ff14SB.xml', 'amber14/tip3p.xml')
# Create Modeller object  This Modeller object will be used in place of the
# actual pdb file.
salt_model = Modeller(salt.topology, salt.positions)

# Add a tip3p waterbox solvent
salt_model.addSolvent(forcefield, model = 'tip3p', padding = 1.5*nanometers)
##################################################################################################################################
# Create and setup the system/environment as well as the integrator
# to be used in the simulation. Values will be recorded at every femtosecond
# (1 femtosecond = 1 timestep), and the system will be set to stay at around
# 296 Kelvin

system = forcefield.createSystem(salt_model.topology, nonbondedMethod = PME, 
                                 nonbondedCutoff = 1.0*nanometers, constraints = HBonds)
integrator = LangevinIntegrator(296*kelvin, 1.0/picosecond, 1.0*femtosecond)

# Specify the platform/processor that will be used to run the simulation on.
# Since the average person will be doing these simulations on their own computer
# with no special modifications, 'CPU' will be the only platform one wll be able
# to use.
platform = Platform.getPlatformByName('CPU')

# Initialize the simulation with the required topology, system, integrator, and
# platform, as well as set the positions of the molecules in the simulation.
simulation = Simulation(salt_model.topology, system, integrator, platform)
simulation.context.setPositions(salt_model.positions)
##################################################################################################################################
#PDB fixer excerpt that gets rogue PDB files working

#Note you need to change the filename in THREE places for each new protein structure

#pdbfixer fixes issues with missing residues, missing H atoms, and adds in solvent


from pdbfixer import PDBFixer
fixer = PDBFixer(filename='1a4b.pdb')
numChains = len(list(fixer.topology.chains()))  #these two lines remove all chains but the first
fixer.removeChains(range(1, numChains)) #these two lines remove all chains but the first
fixer.findMissingResidues()
fixer.findNonstandardResidues()
fixer.replaceNonstandardResidues()
fixer.removeHeterogens(False)  #the "false" also removes waters
fixer.findMissingAtoms()
fixer.addMissingAtoms()
fixer.addMissingHydrogens(7.0)
fixer.addSolvent(fixer.topology.getUnitCellDimensions(), positiveIon='Na+', negativeIon='Cl-', ionicStrength=0.0*molar)
PDBFile.writeFile(fixer.topology, fixer.positions, open('1a4b-fixed.pdb', 'w'))
print('Done writing fixed PDB')
print('Done adding solvent')
#This bit of code will show you if there are any residues that are undefined in the forcefield 
#(like Na+ or Cl- have been problematic in the past)
#NOTE:   the forcefields for ions are in the amber14/tip3p.xml water model forcefield.  
#If you just use "tip3p.xml" it WON'T WORK! OpenMM manual mentions this...
##################################################################################################################################
# Minimization: provides initial low energy structure

# Get the initial state of the system and print out the values for
# potential and kinetic energy
st = simulation.context.getState(getPositions=True, getEnergy=True, enforcePeriodicBox=True)
print("Potential energy before minimization is %s" % st.getPotentialEnergy())
print("Kinetic energy before minimization is %s" % st.getKineticEnergy())

# Minimize the simulation for at most 100 iterations (the simulation 
# can potentially stop minimizing if the kinetic energy has been sufficiently
# minimized before it reaches 100 iterations, although you won't be able
# to tell), while also taking note of how long it takes for the minimization to
# finish.
print('Minimizing...')
tinit = time()
simulation.minimizeEnergy(maxIterations=100)
tfinal = time()

# Get the new state of the system and print out the values for
# potential and kinetic energy.
st = simulation.context.getState(getPositions=True,getEnergy=True, enforcePeriodicBox=True)
print("Potential energy after minimization is %s" % st.getPotentialEnergy())
print("Kinetic energy after minimization is %s" % st.getKineticEnergy())

# Print out the length of time the minimization took to complete.
print("Done Minimization! Time required: ", tfinal-tinit, "seconds")
##################################################################################################################################
# Production: creates trajectory at desired temperature, starting from end of equilibration

# Set up simulation to save important values needed for visualization purposes
# to a PDB file and a DCD file, as well as report the timestep, the kinetic
# and potential energies, and the temperature of the system to the standard
# output, every 100 timesteps.
Nsteps=1000000
print_every_Nsteps=5000
simulation.reporters.append(PDBReporter('salt_trajectory.pdb', print_every_Nsteps))
simulation.reporters.append(StateDataReporter(stdout, print_every_Nsteps, step=True, kineticEnergy=True, 
    potentialEnergy=True, temperature=True, separator='\t'))

# Start the simulation, while also taking note of how long it takes for the
# simulation to finish. When the values are shown in the standard output,
# it will look like the simulation starts at at the 10,000th timestep. That's
# because we are looking at the current state of the system. We already told
# the simulation to go through 10,000 timesteps in the equilibration step, so
# that's what's being reflected here.
tinit = time()
print('Running Production...')
simulation.step(Nsteps)
tfinal = time()
print('Done!')

# Print out the length of time the simulation took to complete.
print('Done production! Time required:', tfinal-tinit, 'seconds')
##################################################################################################################################
# Equilibration: sets initial velocities and brings system up to desired temperature
# Set the system to maintain atom velocities such that the temperature of
# the system fluctuates around 296 Kelvin throughout the rest of the 
# equilibration and final simulation.
simulation.context.setVelocitiesToTemperature(296*kelvin)

# Equilibrate the system for 10,000 timesteps while also taking note of 
# how long it takes for the equilibration to finish.
print('Equilibrating...')
tinit = time()
simulation.step(10000)   #number is how many timesteps of equilibration to do
tfinal = time()

# Print out the length of time the equilibration took to complete.
print("Done equilibrating! Time required:", tfinal - tinit, "seconds")
##################################################################################################################################
# Trajectory analysis using the mdtraj package
import matplotlib.pyplot as plt
import mdtraj as md
import numpy as np

traj = md.load('salt_trajectory.pdb')
print(traj)

print('How many atoms?    %s' % traj.n_atoms)   #prints out number of atoms in simulation
print('How many residues? %s' % traj.n_residues)   #prints out number of residues in simulation
print('Second residue: %s' % traj.topology.residue(1))   #prints out the residue label for the number you put in
atom = traj.topology.atom(2)      #picks out a specific atom (based on the number) for further interrogation
print('''Hi! I am the %sth atom, and my name is %s. 
I am a %s atom with %s bonds. 
I am part of an %s residue.''' % ( atom.index, atom.name, atom.element.name, atom.n_bonds, atom.residue.name))
##################################################################################################################################
#Distance Analysis

plt.plot(md.rmsd(traj,traj[0]), label="RMSD")
plt.plot(md.compute_distances(traj,[[0,1]],periodic=True), label="Na-Cl distance")   #distance between atoms 0 and 1
plt.plot(np.sqrt(np.sum((traj.xyz[0, 1, :] - traj.xyz[:, 1, :])**2, axis=1)), label="Na travel distance")  # travel distance for atom 0
plt.plot(np.sqrt(np.sum((traj.xyz[0, 0, :] - traj.xyz[:, 0, :])**2, axis=1)), label="Cl travel distance")  # travel distance for atom 1
plt.xlabel("Frames")
plt.ylabel("Distance/nm")
plt.legend(loc='upper left',fontsize='medium')

print(np.mean(np.sqrt(np.sum((traj.xyz[:, 0, :] - traj.xyz[:, 1, :])**2, axis=1))))  
#prints mean distance between atoms 0 and 1 over the whole trajectory