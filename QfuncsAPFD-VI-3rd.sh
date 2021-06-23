#!/bin/bash

#SBATCH -t 24:00:00
#SBATCH --job-name="qchem"
#SBATCH --output="qchem%j.%N.out"
#SBATCH --error="qchem%j.%N.err"
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --mem-per-cpu=2G
#SBATCH --export=ALL
#SBATCH --account=smc102

nthreads=4          #How many processors the job will use (match this to the #SBATCH--cpus-per-task line above
jobstem=QfuncsAPFD-VI-3rd #Filename of qchem job file; assumes you use a inp extension so don't include it on this line
jobfile=$jobstem.in
outputfile=$jobstem.out

module purge
module load slurm
module load cpu
module load gcc
module load mvapich2
module load qchem

export QCSCRATCH=/scratch/$USER/job_$SLURM_JOBID      #Tells qchem to write temporary files to the scratch disk on Expanse
exe=`which qchem`
/usr/bin/time $exe -slurm -nt $nthreads $jobfile $outputfile
