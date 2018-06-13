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
            j = 0              #   │
        elif j == 'b':         #   a→0
            j = 1              #   b→1
        elif j == 'c':         #   c→2
            j = 2              #   d→3
        else:                  #   │
            j = 3              #   陣列28*39  
        a.append(j)            #   長度不夠時，其餘→4
        n=n+1                  #   │
    while n<40:                #   │
        a.append(4)            #   │
        n=n+1                  #   │        
    aa=np.array(a)             #   │
    aaa.append(aa)             #   │
new_data=np.array(aaa)         #───┘

states = ["1", "2", "3"]        #─┐
n_states = len(states)          #─┴該HMM有三個狀態{1, 2, 3}

observations = ["a", "b", "c", "d"]    #─┐
n_observations = len(observations)     #─┴每個狀態有四種可能輸出{a, b, c, d}

model = hmm.MultinomialHMM(n_components=n_states)                                                 #───┐
model.fit(new_data) #Estimate model parameters.                                                   #   │ 
print('初始值產生↓↓↓↓↓↓↓↓\n')                                                                      #   HMM model
print ('Initial state occupation distribution: \n',model.startprob_)                              #   │
print ('\nMatrix of transition probabilities between states: \n',model.transmat_)                 #   │
print ('\nProbability of emitting a given symbol when in each state: \n',model.emissionprob_)     #   │
print ('\nCompute the log probability under the model: \n',model.score(new_data))                 #   │
                                                                                                  #   │
model_p = hmm.MultinomialHMM(n_components=n_states)                                               #   │
model_p.startprob_ = model.startprob_                                                             #   │
model_p.transmat_ = model.transmat_                                                               #   │
model_p.emissionprob_ = model.emissionprob_                                                       #───┘






start=1                                                                                           #───┐
while start == 1:                                                                                 #───│
    input_seq = input('請輸入一個序列  (ex:abcddcbaddccbbaa)(結束輸入exit)\n')                      #───簡單介面可以輸入一個序列O
    if input_seq == 'exit':                                                                       #   │
        print('Bye Bye~~')                                                                        #   │
        start=0                                                                                   #   │
    else:                                                                                         #   │
        X=[]                                                                                      #   │
        #預測內部隱藏狀態的最佳順序                                                                 #   show result
        for i in input_seq:                                                                       #   │
           if i == 'a' :                                                                          #   │
               X.append(0)                                                                        #   │
           elif i == 'b':                                                                         #   │
                X.append(1)                                                                       #   │
           elif i == 'c':                                                                         #   │
                X.append(2)                                                                       #   │
           elif i == 'd':                                                                         #   │
                X.append(3)                                                                       #   │
           else:                                                                                  #   │
               print('請輸入{a,b,c,d}組合的字串')                                                  #   │
               start = 0                                                                          #   │
               break                                                                              #   │
        if start == 1:                                                                            #   │
            X=np.atleast_2d(X).T                                                                  #   │
            print('輸出M產生該序列的機率: ', model_p.score(X), '\n')                               #   │
            result1, result2 = model_p.decode(X, algorithm="viterbi")                             #   │
            print('可能產生路徑: ', ', '.join(map(lambda x: observations[int(x)], X)))             #   │
            print('可能產生狀態: ', ', '.join(map(lambda x: states[int(x)], result2)))             #   │
        else:                                                                                     #   │
            start=1      






from sklearn.externals import joblib
#指定名稱
filename = 'model.m'

#調用 DUMP 函數
joblib.dump(model,filename)

# 調用乙存儲模型
model = joblib.load('model.m')
































                                                                         #───┘ 
    