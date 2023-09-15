import gurobipy as gp, numpy as np, math
import sys, os, argparse


def falafel(S,q):
    n,m = S.shape
    

    model = gp.Model()
    model.Params.Threads = args.threads
    model.Params.TimeLimit = args.run_time

    # initialize variables
    R = np.empty(m,dtype=object)
    for j in range(m): 
        R [j]= model.addVar(vtype=gp.GRB.BINARY)

    # set constraints

    for i in range(n):
        model.addConstr(gp.quicksum(R[j]*S[i,j] for j in range(m)) >= q* gp.quicksum(R[j] for j in range(m)))

      

    # set objective
    model.setObjective(gp.quicksum(R[j] for j in range(m)), gp.GRB.MAXIMIZE)

    model.optimize()

    return np.array([j for j in range(m) if R[j].X > 0])




if __name__=="__main__":
    #parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    parser.add_argument('-o', '--output', type=str, required=True)
    parser.add_argument('-q', '--q', type=float, required=True)
    parser.add_argument('-c', '--threads', type=int, required=True)
    parser.add_argument('-t', '--run_time', type=int, required=True)
    args = parser.parse_args(sys.argv[1:])
-r
  

    assert args.q <= 1

    S = np.load(args.input, allow_pickle=True)['m']

   # run falafel
    R_chosen = falafel(S,args.q)
    np.savez(args.output,  cols=R_chosen )