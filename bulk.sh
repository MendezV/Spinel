#!/bin/bash
#SBATCH --partition=nodes
#SBATCH --job-name=Co3O4-bulk
#SBATCH --output=Co3O4-bulk%a.txt
#SBATCH --array=1-2
#SBATCH --exclude=node[1001-1032]
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12


declare -a commands

commands[1]="/home/jfm343/JDFTXDIR/build/jdftx -i latticeOpt.in | tee latticeOpt.out;"
commands[2]="echo done"
bash -c "${commands[${SLURM_ARRAY_TASK_ID}]}"
