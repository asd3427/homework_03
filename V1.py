#import datetime

import numpy as np
import matplotlib.pyplot as plt
from hmmlearn.hmm import GaussianHMM

#from convert_to_timeseries import convert_data_to_timeseries

#load data from txt file
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
    #X=np.append(X, n)
#X.reshape(1, -1)

print(l)



#create and train gaussion hmm
print('Training HMM....')
num_components=3
model = GaussianHMM(n_components=num_components, covariance_type='diag', n_iter=100)
model.fit(X)
#

#predict the hidden states of HMM
hidden_states = model.predict(X)

print('Means and variances of hidden states:')
for i in range(num_components):
        print('Hidden state', i+1)
        print('Mean = ', round(model.means_[i][0], 3))
       # print('Variance = ', round(np.diag(model.covars_[i][0], 3)))
        
        
#Generate data using model        
num_samples = 1000
samples, _ = model.sample(num_samples)
plt.plot(np.arange(num_samples), samples[:,0], c='black')
plt.title('Number of components = ' + str(num_components))

plt.show()
#

