from pomegranate import *
with open ('hmmData.txt') as f :
    data = f.read()
model = HiddenMarkovModel()
model.dense_transition_matrix(data)
