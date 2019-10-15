# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:25:37 2019

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

"""
"Parameters"
tua=1;
#U=0
Delta=0.7;
mu=0.1;

params=np.array([tua,Delta,U,mu])
np.savetxt("params",params)
"""

"Get parameters from the initilization file"
"U is not used"
"mu is divided by 2 since TEBD hits it twice"
params=np.loadtxt("params")
tua=params[0]
Delta=params[1]
U=params[2]
mu=params[3]/2

"Matrix Operators"
def VPOl(V):
    return np.array([I2,(tua+Delta)/2*sx,(tua-Delta)/2*sy,V*sz,-mu*sz])
def MPO(V):
    return np.array([[I2,(tua+Delta)/2*sx,(tua-Delta)/2*sy,V*sz,-mu*sz],[Z2,Z2,Z2,Z2,sx],[Z2,Z2,Z2,Z2,sy],[Z2,Z2,Z2,Z2,sz],[Z2,Z2,Z2,Z2,I2]])
def VPOr(V):
    return np.array([-mu*sz,sx,sy,sz,I2])

"Multiplying two Matrix Operators"
def TimesHMM(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0,0])
    ttp=np.einsum('ijab,jkcd->ikabcd',T1,T2)
    ttp=np.swapaxes(ttp,2,5)
    ttp=np.reshape(ttp,(5,5,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,2,3)
    return ttp
def TimesHVM(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0,0])
    ttp=np.einsum('jab,jkcd->kabcd',T1,T2)
    ttp=np.swapaxes(ttp,1,4)
    ttp=np.reshape(ttp,(5,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,1,2)
    return ttp
def TimesHMV(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0])
    ttp=np.einsum('ijab,jcd->iabcd',T1,T2)
    ttp=np.swapaxes(ttp,1,4)
    ttp=np.reshape(ttp,(5,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,1,2)
    return ttp
def TimesHVV(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0])
    ttp=np.einsum('jab,jcd->abcd',T1,T2)
    ttp=np.swapaxes(ttp,0,3)
    ttp=np.reshape(ttp,(L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,0,1)
    return ttp
"Chooses the correct Matrix Operator Multiplication"
def TimesH(T1,T2):
    if len(np.shape(T1))==4:
        if len(np.shape(T2))==4:
            thtp=TimesHMM(T1,T2)
        elif len(np.shape(T2))==3:
            thtp=TimesHMV(T1,T2)
    elif len(np.shape(T1))==3:
        if len(np.shape(T2))==4:
            thtp=TimesHVM(T1,T2)
        elif len(np.shape(T2))==3:
            thtp=TimesHVV(T1,T2)
    return thtp

"returns the hamiltionian in the wavefunction basis"
def Ht(V,L):
    htp=VPOl(V)
    for i in range(1,L-1):
        htp=TimesH(htp,MPO(V))
    htp=TimesH(htp,VPOr(V))
    return htp