#!/bin/bash
# -*- coding: utf-8 -*-

mkdir -p temp 
mkdir -p log

rm -f temp/snakemake.cmd

echo "sh snakemake.sh " > temp/snakemake.cmd


swarm \
    --file temp/snakemake.cmd \
    --time 0-5:00:00 \
    --logdir log/ \
    --partition ccr,norm \
    -g 100 \
    -t 8 \
    --sbatch "--mail-type=END --mail-user=xli1994@umd.edu"

