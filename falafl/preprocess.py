#!/usr/bin/env python

import numpy as np,pandas as pd
import sys, os, argparse


def get_parser():
    parser = argparse.ArgumentParser()
    #input & output
    parser.add_argument('-i', '--input', type=str, nargs='+',required=True)
    parser.add_argument('-of', '--output_frac', type=str, required=True)
    parser.add_argument('-ob', '--output_bin', type=str, required=True)

    # params
    ## num patients with good coverage
    parser.add_argument('-k', '--k', type=int, required=True)
    ## good overage threshold
    parser.add_argument('-p', '--p', type=float, required=True)
    ## min coverage considered
    #parser.add_argument('-d', '--delta', type=float, required=True)

    return parser

# input should be an npz with the following: patient, frac, site
# def trim_by_min_coverage(f,delta):
#     data = np.load(f,allow_pickle=True)
#     patient,site, frac = data['site'],data['frac'],data['patient']
#     trim_idx =  np.where(frac>= delta)
#     sites_to_keep = site[trim_idx]
#     frac_to_keep = frac[trim_idx]

#     return patient, sites_to_keep, frac_to_keep
    
def concat_data(files):
    sites_dict ={}
    for f in files:
        p = f.split('/')[-1].split('_')[0]
        df =pd.read_csv(f,sep=' ',header=None)
        sites_dict[p] = df
    all_sites = list(set.intersection(*[set(v[0]) for v in sites_dict.values()]))
    #remove sex chromosome sites
    select_sites = sorted([s for s in all_sites if not s.startswith('chrX') and not s.startswith('chrY')])
    concat_list = []
    for k,v in sites_dict.items():
        _v = v.set_index(0) 
        _v.columns = [k]
        _v = _v.loc[select_sites]
        concat_list.append(_v)

    df_frac = pd.concat(concat_list,axis = 1).T


    return df_frac

def process_data(df,p,k):
    m = df.values
    m[m< p]  = 0
    m[m>=p] = 1

    patients = df.index


    print(patients)
    # col_sum = np.sum(m,axis=0)
    # select_col = np.where(col_sum>=k)[0]

    # add new constraints that we need at least 2 from left,1 from right, and 1 from rectum
    # very hacky implementation right now needs update later
    left = m[0:4,:]
    left_p = patients[0:4]
    right = m[4:7,:]
    right_p = patients[4:7]
    rectum = m[7:,:]
    rectum_p = patients[7:]
    print(left_p,right_p,rectum_p)

    select_col_ls=[]

    for subtype,k_ in [(left,2),(right,1),(rectum,1)]:
        col_sum = np.sum(subtype,axis=0)
        select = set(np.where(col_sum>=k_)[0])
        select_col_ls.append(select)

    select_col = sorted(set.intersection(*select_col_ls))


        


    _m = m[:,select_col]
    sites = df.columns[select_col]


    col_sum = np.sum(_m,axis=0)
    select_col_check = np.where(col_sum>=k)[0]

    print(_m.shape, len(select_col_check))


    df_bin = pd.DataFrame(_m,columns = sites, index = df.index)

    return df_bin

def main():
    args = get_parser().parse_args(sys.argv[1:])
    
    df_frac = concat_data(args.input)
    np.savez(args.output_frac,m = df_frac.values, cols = df_frac.columns,rows = df_frac.index)
    
    df_bin = process_data(df_frac, args.p, args.k)
    np.savez(args.output_bin,m = df_bin.values, cols = df_bin.columns,rows = df_bin.index)


if __name__=="__main__":
    #parser
    main()


    



    
    

