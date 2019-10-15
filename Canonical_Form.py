# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:38:39 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:02:24 2019

@author: jsten
"""
import numpy as np
import matplotlib.pyplot as plt
import time
from cmath import *
import scipy.linalg as lng
import copy


def RCon(Mps,l):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp[0])
    L=len(mtp)
    DD=len(mtp[l][0])
    toStack=[mtp[l][0]]
    for d in range(1,dd):
        toStack.append(mtp[l][d])
    stack= np.vstack(toStack)
    SVD=lng.svd(stack,full_matrices=False)
    s=SVD[0]
    DG=np.diag(SVD[1])
    v=SVD[2]
    if l==0:
        mtp[0]=s
        mtp[1]=np.einsum('ij,jk,dkl->dil',DG,v,mtp[1])
    elif l==L-2:
        DDp=len(mtp[l][0][0])
        m0tp=[]
        m1tp=[]
        for d in range(0,dd):
            m0tp.append(s[d*DD:(d+1)*DD,0:DDp])
            m1tp.append(np.dot(DG,np.dot(v,mtp[l+1][d])))
        mtp[l]=np.array(m0tp)
        mtp[l+1]=np.array(m1tp)
    else:
        DDp=len(mtp[l][0][0])
        m0tp=[]
        m1tp=[]        
        for d in range(0,dd):
            m0tp.append(s[d*DD:(d+1)*DD,0:DDp])
            m1tp.append(np.dot(DG,np.dot(v,mtp[l+1][d])))
        mtp[l]=np.array(m0tp)
        mtp[l+1]=np.array(m1tp)
    return mtp


"Transposes a MPS"
def TAll(Mps):
    mtp=copy.deepcopy(Mps)
    mttp=copy.deepcopy(Mps)
    dd=len(mtp[0])
    L=len(mtp)
    mttp[L-1]=mtp[0]
    for l in range(1,L-1):
        mttp[L-l-1]=np.einsum('dij->dji',mtp[l])
    mttp[0]=mtp[L-1]
    return mttp
    

def LCon(Mps,l):
        mtp=copy.deepcopy(Mps)
        L=len(mtp)
        mtp=TAll(mtp)
        mtp=RCon(mtp,L-1-l)
        mtp=TAll(mtp)
        return mtp

def RConAll(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    for l in range(0,L-1):
        mtp=RCon(mtp,l)
    return mtp

def LConAll(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    for l in range(0,L-1):
        mtp=LCon(mtp,L-1-l)
    return mtp

def ConCheck(mps):
    mtp=copy.deepcopy(mps)
    out=[0]*len(mtp)
    tempL=np.einsum('dj,dj->',mtp[0],np.conjugate(mtp[0]))
    tempR=np.einsum('di,dj->ij',np.conjugate(mtp[0]),mtp[0])
    if abs(tempL-1)<10**(-5):
        out[0]="L"
    elif np.amax(abs(tempR-np.identity(len(tempR))))<10**(-5):
        out[0]="R"
    for l in range(1,L-1):
        tempL=np.einsum('djk,dlk->jl',mtp[l],np.conjugate(mtp[l]))
        tempR=np.einsum('dkj,dkl->jl',np.conjugate(mtp[l]),mtp[l])
        if np.amax(abs(tempR-np.identity(len(tempR))))<10**(-5):
            out[l]="R"
        elif np.amax(abs(tempL-np.identity(len(tempL))))<10**(-5):
            out[l]="L"
    tempR=np.einsum('dj,dj->',mtp[L-1],np.conjugate(mtp[L-1]))
    tempL=np.einsum('di,dj->ij',np.conjugate(mtp[L-1]),mtp[L-1])
    if abs(tempR-1)<10**(-5):
        out[L-1]="R"
    elif np.amax(abs(tempL-np.identity(len(tempL))))-1<10**(-5):
        out[L-1]="L"
    return out



"""
y0=RCon(y,0)
y4=LCon(y0,4)
y3=LCon(y4,3)
y2=LCon(y3,2)
y1=LCon(y2,1) 
y2n=RCon(y1,1)
"""
    
"""                
z1=LCon(y,4)
z2=LCon(z1,3)
z3=LCon(z2,2)
z4=LCon(z3,1)
"print(LeftCheck(z4))"



y1=RCon(y,0)
y2=RCon(y1,1)
y3=RCon(y2,2)
y4=RCon(y3,3)
"print(RightCheck(y4))"

m1=RCon(y,0)
m2=RCon(m1,1)
m3=LCon(m2,4)
m4=LCon(m3,3)
print(RightCheck(m4))
print(LeftCheck(m4))

print([E(y,y),E(y4,y4),E(z4,z4),E(m4,m4)])
"""

