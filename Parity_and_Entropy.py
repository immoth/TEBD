# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:39:31 2019

@author: jsten
"""
import numpy.linalg as lng
import MPS


"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
I2=np.dot(sz,sz)
Z2=sz-sz

def RConDG(Mps,l):
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
    return [mtp,SVD[1]]


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
    

def LConDG(Mps,l):
        mtp=copy.deepcopy(Mps)
        L=len(mtp)
        mtp=TAll(mtp)
        [mtp,DG]=RConDG(mtp,L-1-l)
        mtp=TAll(mtp)
        return [mtp,DG]

def entR(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    etp=[]
    for l in range(0,L-1):
        [mps,dg]=RConDG(mps,l)
        ldg=np.log(dg**2)/np.log(2)
        etp.append(-np.dot(dg**2,ldg))
    return etp

def entL(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    etp=[]
    for l in range(0,L-1):
        [mps,dg]=RConDG(mps,l)
    for l in range(L-1,0,-1):
        [mps,dg]=LConDG(mps,l)
        ldg=np.log(dg**2)/np.log(2)
        etp.append(-np.dot(dg**2,ldg))
    return etp
        
    

def apply_x(l,mps):
    mtp=copy.deepcopy(mps)
    if l==0:
        mtp[l]=np.einsum("ab,bi->ai",sx,mtp[l])
    elif l==L-1:
        mtp[l]=np.einsum("ab,bi->ai",sx,mtp[l])
    else:
        mtp[l]=np.einsum("ab,bij->aij",sx,mtp[l])
    return mtp

def apply_z(l,mps):
    mtp=copy.deepcopy(mps)
    if l==0:
        mtp[l]=np.einsum("ab,bi->ai",sz,mtp[l])
    elif l==L-1:
        mtp[l]=np.einsum("ab,bi->ai",sz,mtp[l])
    else:
        mtp[l]=np.einsum("ab,bij->aij",sz,mtp[l])
    return mtp

def parL(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    ptp=[]
    for l in range(0,L):
        mtpz=apply_z(l,mtp)
        ptp.append(MPS.innerMPS(mtp,mtpz))
    return ptp

def totalP(mps):
    mtp=copy.deepcopy(mps)
    mtp0=copy.deepcopy(mps)
    L=len(mtp)
    for l in range(0,L):
        mtp=apply_z(l,mtp)
    ttp=MPS.innerMPS(mtp0,mtp)
    return ttp

def entropy(Mps,l):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp[0])
    L=len(mtp)
    DD=len(mtp[l][0])
    toStack=[mtp[l][0]]
    for d in range(1,dd):
        toStack.append(mtp[l][d])
    stack= np.vstack(toStack)
    SVD=lng.svd(stack,full_matrices=False)
    dg=SVD[1]/np.sqrt(np.dot(SVD[1],SVD[1]))
    dg=dg+[10**-10]*len(dg)
    ldg=np.log(dg**2)/np.log(2)
    etp=-np.dot(dg**2,ldg)
    return etp


def entropyL(mps):
    mtp=copy.deepcopy(mps)
    etp=[]
    for l in range(0,L):
        etp.append(entropy(mtp,l))
    return etp

"For Wave functions"
def bkt(a,b,c):
    return np.dot(np.conjugate(a),np.dot(b,c))

"Kronecker Product for arbitarty number of matrices"
def krn(lis):
    lis_L=len(lis)
    ktp=lis[0]
    for l in range(1,lis_L):
        ktp=np.kron(lis[l],ktp)
    return ktp

"local parity operator"
def Opar(l,L):
        ptpl=[]
        for k in range(0,l):
            ptpl.append(s0)
        ptpl.append(sz)
        for k in range(l+1,L):
            ptpl.append(s0)
        ptp=krn(ptpl)
        return ptp
    
def OparL(psi):
     psitp=copy.deepcopy(psi)
     otp=[]
     L=int(np.log(len(psip))/np.log(2))
     for l in range(0,L):
         otp.append(bkt(psitp,Opar(l,L),psitp))
     return otp





