import os
from myhmm_scaled import MyHmmScaled

#讀取觀察序列
f=open('./hmmData.txt','r')
observation_list=f.readlines()

#進行資料前處理->
observation_listed=[]
for obs in observation_list:
     observation_listed.append(obs.rstrip())

#讀取隨機模型參數
models_dir = os.path.join('.', 'models') #
model_file = "random.json"
hmm = MyHmmScaled(os.path.join(models_dir, model_file))
    
#輸入觀察陣列，使用Baum Welch演算法計算模型參數
hmm.forward_backward_multi_scaled(observation_listed)

#輸出最後產生的模型參數
print("A = ", hmm.A)
print("B = ", hmm.B)
print("pi = ", hmm.pi)
    
#使用Viterbi演算法計算最佳可能路徑 
observations = 'abcddcbaddccbbaa'
prob, hidden_states = hmm.viterbi(observations)
print("Max Probability = ", prob, " Hidden State Sequence = ", hidden_states)