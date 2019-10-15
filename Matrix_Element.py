# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:48:48 2019

@author: jsten
"""

import numpy as np
import copy
import numpy.linalg as lng


"applys an operator an MPS"
def apply_O(Op,mps):
    mtp=copy.deepcopy(mps)
    otp=copy.deepcopy(Op)
    L=len(mtp)
    "l=0"
    [oDDp,odd,oddp]=np.shape(otp[0])
    [mdd,mDDp]=np.shape(mtp[0])
    m0=np.einsum('bfd,fj->dbj',otp[0],mtp[0])
    m1=np.reshape(m0,(odd,oDDp*mDDp))
    mtp[0]=m1
    "0<l<L-1"
    for l in range(1,L-1):
        [oDD,oDDp,odd,oddp]=np.shape(otp[l])
        [mdd,mDD,mDDp]=np.shape(mtp[l])
        m0=np.einsum('abfd,fij->daibj',otp[l],mtp[l])
        m1=np.reshape(m0,(odd,oDD*mDD,oDDp*mDDp))
        mtp[l]=m1
    "l=L-1"
    [oDD,odd,oddp]=np.shape(otp[L-1])
    [mdd,mDD]=np.shape(mtp[L-1])
    m0=np.einsum('afd,fi->dai',otp[L-1],mtp[L-1])
    m1=np.reshape(m0,(odd,oDD*mDD))
    mtp[L-1]=m1
    return mtp

"Computes the matrix element <psi|H|psi>"
def ME(mps1,mpo,mps2):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    mpoH=copy.deepcopy(mpo)
    L=len(mpsA)
    "l=L-1"
    mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
    "L-1>l>0"
    for l in range(2,L):
        mtp=np.einsum('dij,jbk,abdf,flk->ial',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
    "l=0"
    mtp=np.einsum('dj,jak,adf,fk->',mpsA[0],mtp,mpoH[0],np.conjugate(mpsB[0]))
    return mtp

"Returns the effective hamiltonian from the matrix element derivetive"
"has a conditional if k=1"
def dME(mps1,mpo,mps2,k):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    mpoH=copy.deepcopy(mpo)
    L=len(mpsA)    
    dd=len(mpsA[k])
    DD=len(mpsA[k][0])
    DDp=len(mpsA[k][0][0])
    if k>1:
        "l=L-1"
        mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jbk,abdf,flk->ial',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('qbr,abuv->qaruv',mtp,mpoH[k])
        "l=k-1"
        mtp=np.einsum('dip,qbruv,abdf,fls->ialupqvsr',mpsA[k-1],mtp,mpoH[k-1],np.conjugate(mpsB[k-1]))
        "k>l>0"
        for l in range(L-k+2,L):
            mtp=np.einsum('dij,jbkupqvsr,abdf,flk->ialupqvsr',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=0"
        mtp=np.einsum('dj,jakupqvsr,adf,fk->upqvsr',mpsA[0],mtp,mpoH[0],np.conjugate(mpsB[0]))
    elif k==1:
        "l=L-1"
        mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jbk,abdf,flk->ial',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('pbr,abuv->paruv',mtp,mpoH[k])
        "l=k-1=0"
        mtp=np.einsum('dp,qaruv,adf,fs->upqvsr',mpsA[k-1],mtp,mpoH[k-1],np.conjugate(mpsB[k-1]))
    mtp=np.reshape(mtp,(dd*DD*DDp,dd*DD*DDp))
    return mtp
    
   
    
"""
"Computes the matrix element <psi|H|psi>"
def MEo(mps1,mpo,mps2):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    mpoH=copy.deepcopy(mpo)
    L=len(mpsA)
    "l=L-1"
    mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
    "L-1>l>0"
    for l in range(2,L):
        mtp=np.einsum('dij,jak,abdf,flk->ibl',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
    "l=0"
    mtp=np.einsum('dj,jak,adf,fk->',mpsA[0],mtp,mpoH[0],np.conjugate(mpsB[0]))
    return mtp
"""    
    
"""
"Returns the effective hamiltonian from the matrix element derivetive"
"has a conditional if k=1"
def dMEo(mps1,mpo,mps2,k):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    mpoH=copy.deepcopy(mpo)
    L=len(mpsA)    
    dd=len(mpsA[k])
    DD=len(mpsA[k][0])
    DDp=len(mpsA[k][0][0])
    if k>1:
        "l=L-1"
        mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jak,abdf,flk->ibl',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('qar,abuv->qbruv',mtp,mpoH[k])
        "l=k-1"
        mtp=np.einsum('dip,qaruv,abdf,fls->iblupqvsr',mpsA[k-1],mtp,mpoH[k-1],np.conjugate(mpsB[k-1]))
        "k>l>0"
        for l in range(L-k+2,L):
            mtp=np.einsum('dij,jakupqvsr,abdf,flk->iblupqvsr',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=0"
        mtp=np.einsum('dj,jakupqvsr,adf,fk->upqvsr',mpsA[0],mtp,mpoH[0],np.conjugate(mpsB[0]))
    elif k==1:
        "l=L-1"
        mtp=np.einsum('di,adf,fj->iaj',mpsA[L-1],mpoH[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jak,abdf,flk->ibl',mpsA[L-l],mtp,mpoH[L-l],np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('par,abuv->pbruv',mtp,mpoH[k])
        "l=k-1=0"
        mtp=np.einsum('dp,qaruv,adf,fs->upqvsr',mpsA[k-1],mtp,mpoH[k-1],np.conjugate(mpsB[k-1]))
    mtp=np.reshape(mtp,(dd*DD*DDp,dd*DD*DDp))
    return mtp
"""
    
    
    
