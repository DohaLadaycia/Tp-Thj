import numpy as np
dat_mat_projet={1:[[1,0.5,0],[0.5,0.75,1],[1,1,1]],2:[[1,0.5,0],[0.5,0.75,1],[1,1,1]]}
def dominante(dic_mat,numb_j):
   mat1=np.array(dic_mat[numb_j][0])
   for i in range(len(dic_mat[numb_j])-1):
      mat2=np.array(dic_mat[numb_j][i+1])
      if(len(set(mat1[:]>mat2[:]))==1):
         if mat1[:][0]<=mat2[:][0]:
            mat1=mat2
   print(mat1)
   return((mat1[:]>=mat2[:]))
if(len(set(dominante(dat_mat_projet,1)))==1):
  print("est une strategie dominante pour joueur 1!")
else:  print("Il y n'a pas une strategie dominante pour joueur 1!")  
if(len(set(dominante(dat_mat_projet,2)))==1):
  print("est une strategie dominante pour joueur 2!")
else:  print("Il y n'a pas une strategie dominante pour joure 2!")  