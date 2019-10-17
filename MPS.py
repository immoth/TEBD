# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:42:06 2019

@author: jsten
"""

import numpy as np
import copy

"creats a random matrix of size DDxDD"
def M(DD):
    return np.random.uniform(0,1,size=(DD,DD))

"creats a random vector of size DD"
def V(DD):
    return np.random.uniform(0,1,size=DD)

"creats a random matrix product state with L sites and physical dimension dd and bond dimension DD"
"1st index: site, 2nd index: physical, 3rd and 4th index: bond"
def MPS(L,DD,dd):
    mttp=[]
    "l=0"
    for d in range(0,dd):
        mttp.append(V(DD))
    mtp=[np.array(mttp)]
    "1<l<L-2"
    for l in range(1,L-1):
        mttp=[]
        for d in range(0,dd):
            mttp.append(M(DD))
        mtp.append(np.array(mttp))
    "l=L-1"
    mttp=[]
    for d in range(0,dd):
        mttp.append(V(DD))
    mtp.append(np.array(mttp))
    return  mtp

"finds the coeficient given an MPS and a configuration"
def Coef(mps,cfig):
    mtp=copy.deepcopy(mps)
    ctp=mtp[0][cfig[0]]
    L=len(mps)
    for i in range(1,L):
        ctp=np.dot(ctp,mtp[i][cfig[i]])
    return ctp

"returns the inner product of two states described by matrix products"
def innerMPS(mps1,mps2):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    L=len(mpsA)
    "l=L-1"
    itp=np.einsum('di,dj->ij',mpsA[L-1],np.conjugate(mpsB[L-1]))
    "L-1>l>0"
    for l in range(2,L):
        itp=np.einsum('dij,jk,dlk->il',mpsA[L-l],itp,np.conjugate(mpsB[L-l]))
    "l=0"
    itp=np.einsum('di,ij,dj->',mpsA[0],itp,np.conjugate(mpsB[0]))
    return itp

"retruns the derivetive of the inner product"
def dIN(mps1,mps2,k):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    L=len(mpsA)    
    dd=len(mpsA[k])
    DD=len(mpsA[k][0])
    DDp=len(mpsA[k][0][0])
    Idd=np.identity(dd)
    if k>1:
        "L=l-1"
        mtp=np.einsum('di,dj->ij',mpsA[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jk,dlk->il',mpsA[L-l],mtp,np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('de,ik->deik',Idd,mtp)
        "l=k-1"
        mtp=np.einsum('dip,abqr,dls->ilapqbsr',mpsA[k-1],mtp,np.conjugate(mpsB[k-1]))
        "k-1>l>0"
        for l in range(L-k+2,L):
            mtp=np.einsum('dij,jkapqbsr,dlk->ilaqpbsr',mpsA[L-l],mtp,np.conjugate(mpsB[L-l]))
        "l=0"
        mtp=np.einsum('di,ijaqpbsr,dj->aqpbsr',mpsA[0],mtp,np.conjugate(mpsB[0]))
    if k==1:
        "L=l-1"
        mtp=np.einsum('di,dj->ij',mpsA[L-1],np.conjugate(mpsB[L-1]))
        "L-1>l>k"
        for l in range(2,L-k):
            mtp=np.einsum('dij,jk,dlk->il',mpsA[L-l],mtp,np.conjugate(mpsB[L-l]))
        "l=k"
        mtp=np.einsum('de,ik->deik',Idd,mtp)
        "l=k-1=0"
        mtp=np.einsum('dp,abqr,ds->apqbsr',mpsA[k-1],mtp,np.conjugate(mpsB[k-1]))
    mtp=np.reshape(mtp,(dd*DD*DDp,dd*DD*DDp))
    return mtp
    

"returns a normalized MPS from any other MPS"
def nMPS(mps):
    mtp=copy.deepcopy(mps)
    ntp=innerMPS(mtp,mtp)
    dd=len(mtp[0])
    L=len(mtp)
    for l in range(0,L):
        mtp[l]=mtp[l]/np.power(ntp,1/(2*L))      
    return mtp



"creates a binary from an integer (used in PsiFromY)"
def binary(x,L):
    btp=[0]*L
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
            
    return btp

"obtain the wave function from a matrix product state"
def PsiFromY(mps):
    mtp=copy.deepcopy(mps)
    L=len(mtp)
    sL=2**L
    state=[0]*sL
    state=np.array(state)
    state[0]=1
    psi=Coef(mtp,binary(0,L))*state
    for i in range(1,sL):
        state[i-1]=0
        state[i]=1
        psi=psi+Coef(mtp,binary(i,L))*state
    return psi

"add to matrix product states"
def addMPS(y1,y2,sign):
    ypn=copy.deepcopy(y1)
    ymn=copy.deepcopy(y2)
    L=len(ypn)
    dd=len(ypn[0])
    ya=[0]*L
    dd=2
    yad=[0]*dd
    for d in range(0,dd):
        ytp=np.array([ypn[0][d],sign*ymn[0][d]])
        yad[d]=np.reshape(ytp,(len(ypn[0][d])+len(ymn[0][d])))
    ya[0]=yad
    
    for l in range(1,L-1):  
        yad=[0]*dd
        for d in range(0,dd):
            ytp=np.array([[ypn[l][d],0*ymn[l][d]],[0*ypn[l][d],ymn[l][d]]])
            ytp=np.swapaxes(ytp,1,2)
            yad[d]=np.reshape(ytp,(len(ypn[l][d])+len(ymn[l][d]),len(ypn[l][d,0])+len(ymn[l][d,0])))
        ya[l]=np.array(yad)
        
    yad=[0]*dd
    for d in range(0,dd):
        ytp=np.array([ypn[L-1][d],ymn[L-1][d]])
        yad[d]=np.reshape(ytp,(len(ypn[L-1][d])+len(ymn[L-1][d])))
    ya[L-1]=yad
        
    yan=nMPS(ya)
    
    return yan

def MPSshape(mps):
    mtp=copy.deepcopy(mps)
    stp=[]
    L=len(mtp)
    for l in range(0,L):
        stp.append(np.shape(mtp[l]))
    return stp

"""
"remember to keep track of the transpose if you reverse order"
def innerMPS2(mps1,mps2):
    mpsA=copy.deepcopy(mps1)
    mpsB=copy.deepcopy(mps2)
    L=len(mpsA)
    "l=L-1"
    itp=np.einsum('di,dj->ij',mpsA[0],np.conjugate(mpsB[0]))
    "L-1>l>0"
    for l in range(1,L-1):
        itp=np.einsum('dji,jk,dkl->il',mpsA[l],itp,np.conjugate(mpsB[l]))
    "l=0"
    itp=np.einsum('di,ij,dj->',mpsA[L-1],itp,np.conjugate(mpsB[L-1]))
    return itp
print(innerMPS(x,x))
print(innerMPS2(x,x))
"""

"""
print(np.einsum('ai,bij,cjk,dk,dl,cml,bnm,an->',x[0],x[1],x[2],x[3],x[3],x[2],x[1],x[0]))
"""

"""
def MPScheck(L,DD,dd):
    mttp=[]
    for d in range(0,dd):
        mtp=[x[0][d]]
        for l in range(1,L-1):
            mtp.append(x[l][d])
        mtp.append(x[L-1][d])
        mttp.append(mtp)
    return  mttp

xx=MPScheck(5,3,2)
print(Norm(xx,xx))
print(innerMPS(x,x)) 
"""  
    
    