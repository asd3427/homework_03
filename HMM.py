import numpy as np
import pandas as pd 
from hmmlearn import hmm

with open ('hmmData.txt') as f:
    data = f.read()
    f.close()
data=data.split('\n')


l=[]
for i in data:
    n=[]
    for a in i:
        n.append(a)
    l.append(n)
l= np.array(l)

n_state = ['1','2','3']
observations=['a','b','c','d']
n_observations = len(observations)
cc = hmm.GaussianHMM(n_components=n_state,startprob_prior=l,transmat_prior=l)
print(cc)

cc.fit()
#inpuT = np.array([x for x in input().split()])
#ll=[]
#
#for i in inpuT:
#    seen = []
#    for a in i:
#        seen.append(a)
#    seen.append(n)
#logprob, box = cc.decode(seen, algorithm="viterbi")
#
#print("The ball picked:", ", ".join(map(lambda x: observations[x], seen)))
#print("The hidden box", ", ".join(map(lambda x: states[x], box)))
