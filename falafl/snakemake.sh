#!/bin/bash
# -*- coding: utf-8 -*-

module load gurobi
module load snakemake

cd /home/lix32/data/FALAFEL/falafl

snakemake --cores 4 --config i=$1
