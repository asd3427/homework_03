import numpy as np
import pandas as pd 


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
data= list(l)

#for i in list:
#    n=[]
#    for a in i:
        
#
###
##import numpy as np
##with open ('hmmData - 複製.txt')  as f :
##    data = f.read()
##
##data =np.array(data)
#print(data[0:0:1])
#data= pd.read_csv('hmmData.txt',header =None )
#print(data)

