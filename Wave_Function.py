# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:38:02 2019

@author: jsten
"""

import numpy as np
import copy

"creates a binary from an integer"
def binary(x,L):
    btp=np.zeros(L)
    for i in range(0,x):
        chk=0
        j=0
        while chk==0:
            if btp[j]==0:
                btp[j]=1
                chk=5
            else:
                btp[j]=0
                j+=1
            
    return btp.astype(int)

"finds the coeficient given an MPS and a configuration"
def Coef(mps,cfig):
    mtp=copy.deepcopy(mps)
    ctp=mtp[0][cfig[0]]
    L=len(mps)
    for i in range(1,L):
        ctp=np.dot(ctp,mtp[i][cfig[i]])
    return ctp

"turns an MPS into a wavefunction"
def wave(mps):
    mpsA=copy.deepcopy(mps)
    L=len(mpsA)
    NoStates=np.power(2,L)
    wtp=np.zeros(NoStates)
    for i in range(0,NoStates):
        cfig=binary(i,L)
        coef=Coef(mpsA,cfig)
        wtp[i]=coef
    return wtp

"bracket"
def bkt(psi1,hw,psi2):
    return np.einsum('i,ij,j->',psi1,hw,psi2)
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    