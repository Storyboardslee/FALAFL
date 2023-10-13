#!/usr/bin/env python

import numpy as np,pandas as pd
import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    #input & output
    parser.add_argument('-i', '--input', type=str, nargs='+',required=True)
    parser.add_argument('-o', '--output', type=str, required=True)
    # params
    ## num patients with good coverage
    parser.add_argument('-k', '--k', type=int, required=True)
    ## good overage threshold
    parser.add_argument('-p', '--p', type=float, required=True)
    ## min coverage considered
    parser.add_argument('-d', '--delta', type=float, required=True)

    return parser

# input should be an npz with the following: patient, frac, site
def trim_by_min_coverage(f,delta):
    data = np.load(f,allow_pickle=True)
    patient,site, frac = data['site'],data['frac'],data['patient']
    trim_idx =  np.where(frac>= delta)
    sites_to_keep = site[trim_idx]
    frac_to_keep = frac[trim_idx]

    return patient, sites_to_keep, frac_to_keep
    
def concat_datad(f_lst):
    

