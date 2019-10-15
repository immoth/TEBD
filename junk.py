# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:40:35 2019

@author: jsten
"""
import MPO
import Matrix_Element as ME
import MPS

no=0
for l in range(0,L):
    no+=ME.ME(ymn,gxlMPO(1,L),MPO.apply_O(gylMPO(1,L),ymn))
    
def MPS1(k,L):
    mtp=[]
    if k==0:
        V=np.array([[1/2,1/2],[0,0]])
    else:
        V=np.array([[0,0],[1/2,1/2]])
    mtp.append(V)
    for l in range(1,L-1):
        if k==l:
            M=np.array([[[1,0],[0,1]],[[0,0],[0,0]]])
        else:
            M=np.array([[[0,0],[0,0]],[[1,0],[0,1]]])
        mtp.append(M)
    if k==L-1:
        V=np.array([[1,1],[0,0]])
    else:
        V=np.array([[0,0],[1,1]])
    mtp.append(V)
    return mtp