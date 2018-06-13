import numpy as np            #─┐
from hmmlearn import hmm      #─┴載入套件

with open('hmmData.txt') as f: #─┐ 
    data=f.read()              # │
    f.close()                  # read txt file
data=data.split('\n')          #─┘

d_n=0                          #───┐                          
for i in data:                 #   │
    m=len(i)                   #   28*39
    if m>=d_n:                 #   │
        d_n=m                  #───┘      
    

aa=[]                          #───┐ 
aaa=[]                         #   │
new_data=[]                    #   │
for i in data:                 #   │
    a=[]                       #   │
    n=1                        #   │
    for j in i:                #   │
        if j == 'a':           #   資料前處理
            j = 1              #   │
        elif j == 'b':         #   a→1
            j = 2              #   b→2
        elif j == 'c':         #   c→3
            j = 3              #   d→4
        else:                  #   │
            j = 4              #   陣列28*39  
        a.append(j)            #   長度不夠時，其餘→0
        n=n+1                  #   │
    while n<40:                #   │
        a.append(0)            #   │
        n=n+1                  #   │        
    aa=np.array(a)             #   │
    aaa.append(aa)             #   │
new_data=np.array(aaa)         #───┘

states = ["1", "2", "3"]        #─┐
n_states = len(states)          #─┴該HMM有三個狀態{1, 2, 3}

observations = ["a", "b", "c", "d"]    #─┐
n_observations = len(observations)     #─┴每個狀態有四種可能輸出{a, b, c, d}

model = hmm.MultinomialHMM(n_components=n_states)   #─┐HMM model
model.fit(new_data) #Estimate model parameters.

print ('Initial state occupation distribution: \n',model.startprob_)
print ('\nMatrix of transition probabilities between states: \n',model.transmat_)
print ('\nProbability of emitting a given symbol when in each state: \n',model.emissionprob_)
print ('\nCompute the log probability under the model: \n',model.score(new_data))

