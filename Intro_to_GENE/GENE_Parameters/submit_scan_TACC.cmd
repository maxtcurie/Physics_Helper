#!/bin/bash
#SBATCH -J GENE        # Job Name
#SBATCH -A GKIMP		# project name
#SBATCH -o GENE.out%j    # Output and error file name (%j expands to jobID)
#SBATCH -N 15
#SBATCH -n 960           # Total number of mpi tasks requested, n=N*64
#SBATCH -p development  # Queue (partition) name -- normal, development, etc.
#SBATCH -t 1:30:00     # Run time (hh:mm:ss) - 1.5 hours
./scanscript --np 32 --ppn 16 --syscall 'ibrun ./gene_stampede'
#ibrun ./gene_stampede2           # Run the MPI executable named a.out  sbatch submit.cmd, showq -u
