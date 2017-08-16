''' A python Program to Check if a path exits from the beginning of an N*N matrix at position (0,0) through the end position (n,n) ..
    
    A path exits if the elements can be connected to each other through 1's
'''



import numpy as np
import pdb
import sys

a = np.array(([1,1,1,1,1],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,0,1,1,1]))
n = a.shape[0]

def nbr(i,j):
    if (i > n-1 or i < 0) or (j > n-1 or j < 0):
        return False
    else:
        if (j== n-1) and (i==n-1):
            print "Path exists"
            sys.exit()
        else:
            if a[i][j] == 1:
                return True
            else :
                return False
    return False

def func(i,j):
    if (i >= n) or (j >=n):
        return False
    if nbr(i+1,j+1):
         func(i+1,j+1)
    if nbr(i+1,j):
         func(i+1,j)
    if nbr(i+1,j-1):
         func(i+1,j-1)
    if nbr(i,j+1):
         func(i,j+1)
    if i>0:
        if nbr(i,j-1):
            func(i,j-1)
    else :
        print "Path doesnt exits"
        sys.exit()
    
    
        
                

if (a[0][0] and a[-1][-1]) == 1:
    func(0,0)
