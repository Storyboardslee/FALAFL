import numpy as np,pandas as pd
import sys, os, argparse


def get_parser():
    parser = argparse.ArgumentParser()
    #input & output
    parser.add_argument('-if', '--input_falafl_sites', type=str, required=True)
    parser.add_argument('-is', '--input_all_sites', type=str, required=True)
    parser.add_argument('-o', '--output', type=str, required=True)

    return parser

def main():

    args = get_parser().parse_args(sys.argv[1:])
    print(args.input_falafl_sites)
    print(args.input_all_sites)
    falafl_sites_idx = np.load(args.input_falafl_sites,allow_pickle=True)
    
    all_sites = np.load(args.input_all_sites,allow_pickle=True)['cols']
    
    falafl_sites = all_sites[falafl_sites_idx]

    with open(args.output) as f: 
        for s in falafl_sites:
            f.write("{}\n".format(s))

    print(len(falafl_sites))



if __name__=="__main__":
    #parser
    main()