# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:29:43 2019

@author: jsten
"""

import numpy as np
import copy
import scipy.linalg as lng
import time
import H_time_mu

cut=20

"keep in mind that this calculation takes considers mu to be 1/2*mu"
def U2(V,dt,s):
    htp=H_time_mu.Ht(V,2)
    utp=lng.expm(1j*htp*dt)
    if s==-1:
        utp=np.conjugate(np.transpose(utp))
    utp=np.reshape(utp,(2,2,2,2))
    return utp

def U1(V,dt,s):
    htp=H_time_mu.VPOr(V)[0]
    utp=lng.expm(1j*htp*dt)
    if s==-1:
        utp=np.conjugate(np.transpose(utp))
    return utp


   
def Apply_Uleft(mps,V,dt,s):
    y0=copy.deepcopy(mps)
    L=len(y0)
    "l=0"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[0])
    y0[0]=M
    "double site operators"
    for l in range(0,L-1):
        if l==0:
            "y0=copy.deepcopy(y)"
            L=len(y0)
            dd=len(y0[l])
            DDp2=len(y0[l][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cj,djk->abk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            Sr=np.reshape(mS,(dd,dd))
            Vr=np.reshape(mV,(dd,dd,DDp3))
            Vr=np.swapaxes(Vr,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
#            y0[l]=Sr[:,0:DDp2]
#            y0[l+1]=Vr[:,0:DD3,:]
        elif l<L-2:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cij,djk->aibk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd*DD2,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            bond=min(dd*DD2,dd*DDp3)
            Sr=np.reshape(mS,(dd,DD2,bond))
            Vr=np.array(np.split(mV,dd,axis=1))
            
            bondc=min(bond,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
            #y0[l]=Sr[:,:,0:DDp2]
            #y0[l+1]=Vr[:,0:DD3,:]
        else:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            M=np.einsum('abcd,cij,dj->aib',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd*DD2,dd))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            Sr=np.reshape(mS,(dd,DD2,dd))
            Vr=np.swapaxes(mV,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc]
            #y0[l]=Sr[:,:,0:DDp2]
            #y0[l+1]=Vr[:,0:DD3]
    "l=L-1"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[L-1])
    y0[L-1]=M
    return y0


def Apply_Uright(mps,V,dt,s):
    y0=copy.deepcopy(mps)
    L=len(y0)
    "l=L-1"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[L-1])
    y0[L-1]=M
    "double site operators"
    for l in range(L-2,-1,-1):
        if l==L-2:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            M=np.einsum('abcd,dj,cij->aib',U2(V,dt,s),y0[l+1],y0[l])
            Mp=np.reshape(M,(dd*DD2,dd))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mDg=np.diag(SVD[1])
            mS=np.dot(SVD[0],mDg)
            mV=SVD[2]
            
            Sr=np.reshape(mS,(dd,DD2,dd))
            Vr=np.swapaxes(mV,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc]
        elif l>0:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cij,djk->aibk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd*DD2,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mDg=np.diag(SVD[1])
            mS=np.dot(SVD[0],mDg)
            mV=SVD[2]
            
            bond=min(dd*DD2,dd*DDp3)
            Sr=np.reshape(mS,(dd,DD2,bond))
            Vr=np.array(np.split(mV,dd,axis=1))
            
            bondc=min(bond,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
        else:
            "y0=copy.deepcopy(y)"
            L=len(y0)
            dd=len(y0[l])
            DDp2=len(y0[l][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cj,djk->abk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mDg=np.diag(SVD[1])
            mS=np.dot(SVD[0],mDg)
            mV=SVD[2]
            
            Sr=np.reshape(mS,(dd,dd))
            Vr=np.reshape(mV,(dd,dd,DDp3))
            Vr=np.swapaxes(Vr,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
    "l=0"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[0])
    y0[0]=M
    return y0


"""
def Apply_Uright(mps,V,dt,s):
    y0=copy.deepcopy(mps)
    L=len(y0)
    "l=L-1"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[L-1])
    y0[L-1]=M
    "double site operators"
    for l in range(0,L-1):
        if l==0:
            "y0=copy.deepcopy(y)"
            L=len(y0)
            dd=len(y0[l])
            DDp2=len(y0[l][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cj,djk->abk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            Sr=np.reshape(mS,(dd,dd))
            Vr=np.reshape(mV,(dd,dd,DDp3))
            Vr=np.swapaxes(Vr,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
            #y0[l]=Sr[:,0:DDp2]
            #y0[l+1]=Vr[:,0:DD3,:]
        elif l<L-2:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            DDp3=len(y0[l+1][0][0])
            M=np.einsum('abcd,cij,djk->aibk',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd*DD2,dd*DDp3))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            bond=min(dd*DD2,dd*DDp3)
            Sr=np.reshape(mS,(dd,DD2,bond))
            Vr=np.array(np.split(mV,dd,axis=1))
            
            bondc=min(bond,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc,:]
            #y0[l]=Sr[:,:,0:DDp2]
            #y0[l+1]=Vr[:,0:DD3,:]
        else:
            dd=len(y0[l])
            DD2=len(y0[l][0])
            DDp2=len(y0[l][0][0])
            DD3=len(y0[l+1][0])
            M=np.einsum('abcd,cij,dj->aib',U2(V,dt,s),y0[l],y0[l+1])
            Mp=np.reshape(M,(dd*DD2,dd))
            
            SVD=lng.svd(Mp,full_matrices=False)
            mS=SVD[0]
            mDg=np.diag(SVD[1])
            mV=np.dot(mDg,SVD[2])
            
            Sr=np.reshape(mS,(dd,DD2,dd))
            Vr=np.swapaxes(mV,0,1)
            
            bondc=min(dd,cut)
            y0[l]=Sr[:,:,0:bondc]
            y0[l+1]=Vr[:,0:bondc]
            #y0[l]=Sr[:,:,0:DDp2]
            #y0[l+1]=Vr[:,0:DD3]
    "l=0"
    M=np.einsum('ab,bi->ai',U1(V,dt,s),y0[0])
    y0[0]=M
    return y0
"""









