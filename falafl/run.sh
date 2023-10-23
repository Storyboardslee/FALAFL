#!/bin/bash
# -*- coding: utf-8 -*-

mkdir -p temp 
mkdir -p log

rm -f temp/snakemake.cmd
for i in {0..35}
do
    echo "sh snakemake.sh $i" >> temp/snakemake.cmd
done

swarm \
    --file temp/snakemake.cmd \
    --time 0-2:00:00 \
    --logdir log/ \
    --partition ccr,norm \
    -g 60 \
    -t 4 \
    --bundle 3 \
    --sbatch "--mail-type=END --mail-user=xli1994@umd.edu"

