# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:49:00 2019

@author: jsten
"""

import numpy as np


"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
I2=np.dot(sz,sz)
Z2=sz-sz


def pVl(p):
    return np.array([I2,p*sz])
    
pM=np.array([[I2,Z2],[Z2,sz]]);
pVr=np.array([I2,sz])

""
def P_MPO(p,L):
    ptp=[0.5*pVl(p)]
    for l in range(0,L-2):
        ptp.append(pM)
    ptp.append(pVr)
    return ptp

"Multiplying two Matrix Operators"
def TimesOMM(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0,0])
    B=len(T1[0,0,0])
    ttp=np.einsum('ijab,jkcd->ikacbd',T1,T2)
    ttp=np.reshape(ttp,(B,B,L1*L2,L1*L2))
    return ttp
def TimesOVM(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0,0])
    B=len(T2[0,0,0])
    ttp=np.einsum('jab,jkcd->kacbd',T1,T2)
    ttp=np.reshape(ttp,(B,L1*L2,L1*L2))
    return ttp
def TimesOMV(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0])
    B=len(T1[0,0,0])
    ttp=np.einsum('ijab,jcd->iacbd',T1,T2)
    ttp=np.reshape(ttp,(B,L1*L2,L1*L2))
    return ttp
def TimesOVV(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0])
    ttp=np.einsum('jab,jcd->acbd',T1,T2)
    ttp=np.reshape(ttp,(L1*L2,L1*L2))
    return ttp
"Chooses the correct Matrix Operator Multiplication"
def TimesO(T1,T2):
    if len(np.shape(T1))==4:
        if len(np.shape(T2))==4:
            thtp=TimesOMM(T1,T2)
        elif len(np.shape(T2))==3:
            thtp=TimesOMV(T1,T2)
    elif len(np.shape(T1))==3:
        if len(np.shape(T2))==4:
            thtp=TimesOVM(T1,T2)
        elif len(np.shape(T2))==3:
            thtp=TimesOVV(T1,T2)
    return thtp

"defines the parity projection operator that acts on wave functions"
def Pt(p,L):
    ptp=pVl(p)
    for i in range(0,L-2):
        ptp=TimesO(ptp,pM)
    ptp=TimesO(ptp,pVr)/2
    return ptp
        
        
        
        
        
        
        
        
        
        
        
        
    
