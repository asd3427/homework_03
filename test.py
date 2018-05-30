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
