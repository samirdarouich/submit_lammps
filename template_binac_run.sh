#!/bin/bash
#{{x.sub}} -q {{x.q}}
#{{x.sub}} -l nodes={{x.N}}:ppn={{x.n}}
#{{x.sub}} -l walltime={{x.time}}
#{{x.sub}} -j oe
#{{x.sub}} -N {{x.jobname}}
#{{x.sub}} -o {{x.job.0}}/{{x.out}}
#{{x.sub}} -l mem={{x.mem}}mb

# Load standard enviroment

module purge
module load mpi/openmpi/3.1-gnu-9.2

# Specify job directory and input file

v_dir={{x.job.0}}
v_input={{x.job.1}}

cd $v_dir
echo Submitting LAMMPS file: $v_input
mpirun --bind-to core --map-by core -report-bindings lmp -i $v_input -var seed $RANDOM
