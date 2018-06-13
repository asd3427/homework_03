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

with open ('hmmData.txt') as f:
    data = f.read()
    f.close()
data=data.split('\n')
#c=np.array('aaaaaaaaa')
l=[]
for i in data:
    n=[]
    for a in i:
        n.append(a)
    l.append(n)



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
