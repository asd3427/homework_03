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
