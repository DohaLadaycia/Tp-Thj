import numpy as np
dat_mat_projet={1:[[0.75,0.5,0.5],[0.37,0.75,0.5],[0.5,0.5,0.99]],2:[[0.75,0.5,0.5],[0.37,0.75,0.5],[0.5,0.5,0.99]]}
def nash (dic_mat):
        best=[]
        nash_list=[]
        for i in range (len(dic_mat)):
          best.append(np.argmax(dic_mat[i+1],axis=0))
        for j in range (len(best)):
           if (j==1):
              nash_list .append([(k, best[j][k]) for k in range(len(best[j]))]) 
           else:
               nash_list .append([(best[j][k],k) for k in range(len(best[j]))]) 
        print(nash_list)
        return list(set(nash_list[0]) & set(nash_list[1]))
print(nash(dat_mat_projet))