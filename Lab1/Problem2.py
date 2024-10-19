import numpy as np
import matplotlib.pyplot as plt 

def dotproduct(Vec1,Vec2):
   p=0
   for i in range(0,max(Vec1.shape[0],Vec2.shape[0])):
     p+=Vec1[i]*Vec2[i] 

   return p


def magnitude(Vec1):
   mag=0
   for i in range(0,Vec1.shape[0]):
      mag+=Vec1[i]**2

   return np.sqrt(mag)

def sum(Mat1,Mat2):
   s=0
   for i in range(0,max(Mat1.shape[0],Mat2.shape[0])):

      for j in range(0,max(Mat1.shape[1],Mat2.shape[1])):

         s+=Mat1[i,j]+Mat2[i,j] 
   return s

def mult(Mat1,Mat2):
   m=0
   for i in range(0,max(Mat1.shape[0],Mat2.shape[0])):

      for j in range(0,max(Mat1.shape[1],Mat2.shape[1])):

         m+=Mat1[i,j]*Mat2[i,j] 
   return m


V=np.array([1,3,5])
W=np.array([0,-1,2])


o=np.arccos(dotproduct(V,W)/(magnitude(V)*magnitude(W)))

print('The angle is',o,'rad')


A=np.array([[7,5,2,1],
            [3,9,2,2],
            [1,2,3,-2]])
B=np.array([[-1,-1,2,1],
             [0,-1,2,-2],
             [0,1,-1,-1]])

print('A+B=',sum(A,B))


C=np.array([[7,5],
            [3,9],
            [1,2]])

D=np.array([[1,2,3,4],
            [5,6,7,8]])

print('C*D=',mult(C,D))
