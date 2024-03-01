#!/bin/bash
#{{x.sub}} -N {{x.N}}
#{{x.sub}} -n {{x.n}}
#{{x.sub}} -t {{x.time}}
#{{x.sub}} -p {{x.node}}
#{{x.sub}} -J {{x.jobname}}
#{{x.sub}} -o {{x.job.0}}/{{x.out}}
#{{x.sub}} --mem-per-cpu={{x.mem_per_cpu}}

module purge
module load compiler/gnu/10.2
module load mpi/openmpi/4.1

v_dir={{x.job.0}}
v_input={{x.job.1}}

cd $v_dir
echo Submitting LAMMPS file: $v_input
mpirun --bind-to core --map-by core -report-bindings lmp -i $v_input

