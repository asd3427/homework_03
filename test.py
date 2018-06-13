<<<<<<< HEAD
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
=======
<<<<<<< HEAD

def splitlist(l,o):
    if isinstance(l,list):
        result= []
        for i in range(l.count(o)):
            end  =l.index(o,0,len(l))
            result.append(l[0:end])
            l = l[end + 1:len(l)]
        if len(l) != 0:
            result.append(l)
        return result
with open("hmmData.txt")  as f :
    data = f.read()
    f.close()
labeList=[]
for row in data:
    labeList.append(row[len(row)-1])
if __name__ =="__main__":
    data = splitlist(labeList,'\n')






hex('a')
=======
import numpy as np
from hmmlearn.hmm import MultinomialHMM
import hmmlearn
from sklearn.feature_extraction import DictVectorizer
>>>>>>> f186aa8dd4cb04b8a766f7646d96191f841f399d


from sklearn.externals import joblib
#指定名稱
filename = 'model.m'

#調用 DUMP 函數
joblib.dump(model,filename)

<<<<<<< HEAD
# 調用乙存儲模型
model = joblib.load('model.m')
=======
start_probability = np.asarray([0.4, 0.3,0.2,0.1])  # guess
transition_probability = np.asarray([[0.4, 0.3], [0.2, 0.1],[0.4,0.2],[0.3,0.1]])
emission_probability = np.array([[0.9, 0.1], [0.1, 0.9]])
model = hmmlearn.hmm.GaussianHMM(n_components=3, verbose=True, n_iter=1000, tol=1e-3)
model.startprob = start_probability
model.transmat = transition_probability
model.emissionprob_ = emission_probability 
model.init_params = 'st'
model.fit(l)
>>>>>>> 6c0d1261760a1b6398272b200eb5bdc5b07f48c5
>>>>>>> f186aa8dd4cb04b8a766f7646d96191f841f399d
