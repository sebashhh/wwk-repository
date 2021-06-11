#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH --job-name="gaussian"
#SBATCH --output="gaussian.%j.%N.out"
#SBATCH --error="gaussian.%j.%N.err"
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=3GB
#SBATCH --account=smc102
#SBATCH --export=ALL

jobstem=TITLE #Filename of Gaussian job file; assumes you use a gjf extension so don't include it on this line
jobfile=$jobstem.gjf
outputfile=$jobstem.log

module purge
module load cpu
module load gaussian/16.C.01
export GAUSS_SCRDIR=/scratch/$USER/job_$SLURM_JOBID      #Tells Gaussian to write temporary files to the scratch disk
exe=`which g16`

bash ./getcpusets $$
cat $$.out $jobfile >file.tmp.$$
/usr/bin/time $exe < file.tmp.$$ > $outputfile
rm -f $$.out file.tmp.$$
