# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:18:41 2019

@author: jsten
"""
import numpy as np
import copy

"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
I2=np.dot(sz,sz)
Z2=sz-sz

"Parameters"
tua=1;
Delta=0.7;
U=0.0;
mu=0.2;

"Matrix Operators"
VPOl=np.array([I2,(tua+Delta)/2*sx,(tua-Delta)/2*sy,U*sz,-mu*sz])
MPO=np.array([[I2,(tua+Delta)/2*sx,(tua-Delta)/2*sy,U*sz,-mu*sz],[Z2,Z2,Z2,Z2,sx],[Z2,Z2,Z2,Z2,sy],[Z2,Z2,Z2,Z2,sz],[Z2,Z2,Z2,Z2,I2]])
VPOr=np.array([-mu*sz,sx,sy,sz,I2])

"constructs the MPO for a given length"
def HMPO(L):
    htp=[VPOl]
    for i in range(1,L-1):
        htp.append(MPO)
    htp.append(VPOr)
    return htp

"Multiplying two Matrix Operators from the hamiltonian"
"I think cd->dc in the output.  See general case below.  This does not affect the current hamiltonian"
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
def Hwave(L):
    htp=VPOl
    for i in range(1,L-1):
        htp=TimesH(htp,MPO)
    htp=TimesH(htp,VPOr)
    return htp


"Multiplying two Matrix Operators"
def TimesMM(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0,0])
    B1=len(T1)
    B2=len(T2)
    ttp=np.einsum('ijab,jkcd->ikabdc',T1,T2)
    ttp=np.swapaxes(ttp,2,5)
    ttp=np.reshape(ttp,(B1,B2,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,2,3)
    return ttp
def TimesVM(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0,0])
    B1=len(T1)
    ttp=np.einsum('jab,jkcd->kabdc',T1,T2)
    ttp=np.swapaxes(ttp,1,4)
    ttp=np.reshape(ttp,(B1,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,1,2)
    return ttp
def TimesMV(T1,T2):
    L1=len(T1[0,0])
    L2=len(T2[0])
    B2=len(T2)
    ttp=np.einsum('ijab,jcd->iabdc',T1,T2)
    ttp=np.swapaxes(ttp,1,4)
    ttp=np.reshape(ttp,(B2,L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,1,2)
    return ttp
def TimesVV(T1,T2):
    L1=len(T1[0])
    L2=len(T2[0])
    ttp=np.einsum('jab,jcd->abdc',T1,T2)
    ttp=np.swapaxes(ttp,0,3)
    ttp=np.reshape(ttp,(L1*L2,L1*L2))
    ttp=np.swapaxes(ttp,0,1)
    return ttp


"retruns the matrix operator from an MPO"
def MPOtoO(mpo):
    mtp=copy.deepcopy(mpo)
    L=len(mtp)
    otp=TimesVM(mtp[0],mtp[1])
    for l in range(2,L-1):
        otp=TimesVM(otp,mtp[l])
    otp=TimesVV(otp,mtp[L-1])
    return otp
    


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




















"Some Tests"
"""
H1=TimesH(VPOl,MPO)
H2=TimesH(H1,VPOr)
H2=np.real(np.round(H2,1))
print(np.amax(H2-Ht))
"""


"""
H1=TimesH(VPOl,MPO)
H2=TimesH(H1,MPO)
H3=TimesH(H2,VPOr)
H3=np.real(np.round(H3,1))
"""

"""
H1=TimesH(VPOl,MPO)
H2=TimesH(H1,MPO)
H3=TimesH(H2,MPO)
H4=TimesH(H3,VPOr)
H4=np.real(np.round(H4,1))
"""

