import numpy as np
import pandas as pd 
from hmmlearn import hmm

with open ('hmmData.txt') as f:
    data = f.read()
    f.close()
data=data.split('\n')


labeList=[]
l=[]
for i in data:
    n=[]
    for a in i:
        n.append(a)
    l.append(n)



states = ["1", "2","3"]##隐藏状态
n_states = len(states)##隐藏状态长度
  
observations = ["a", "b", "c","d"]##可观察的状态
n_observations = len(observations)##可观察序列的长度
  
model = hmm.MultinomialHMM(n_components=n_states, n_iter=1000, tol=0.01)
X = l

model.fit(X)
print (model.startprob_)
print (model.transmat_)
print (model.emissionprob_)

print (model.score(X))
model.fit(X)
print (model.startprob_)
print (model.transmat_)
print (model.emissionprob_)
 #和第一次fit(X)得到的行顺序不一样
# [[  5.55555556e-01   4.44444444e-01   9.29759770e-28]
#  [  1.11111111e-01   2.22222222e-01   6.66666667e-01]]
print (model.score(X))
model.fit(X)
print (model.startprob_)
print (model.transmat_)
print (model.emissionprob_)
print (model.score(X))
 # 可以进行多次fit,然后拿评分最高的模型，就可以预测了
print (model.predict(bob_Actions, lengths=None))
 # 预测最可能的隐藏状态
 # 例如:
 # [0 1 0 0 0 1]
print (model.predict_proba(bob_Actions, lengths=None))# 预测各个隐藏状态的概率
 # 例如:
 # [[ 0.82770645  0.17229355]
 #  [ 0.27361913  0.72638087]
 #  [ 0.58700959  0.41299041]
 #  [ 0.69861348  0.30138652]
 #  [ 0.81799813  0.18200187]
 #  [ 0.24723966  0.75276034]]
 # 在生成的模型中，可以随机生成随机生成一个模型的Z和X
X,Z = model.sample(n_samples=5, random_state=None)



