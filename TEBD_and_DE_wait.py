# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:03:07 2019

@author: jsten
"""

import copy
import numpy as np
import MPS
import scipy.linalg as lng
import U_MPO
import MPO
import Matrix_Element as ME
import Zap
import time
import H_time
import MPO_time


phA=[]
phB=[]
lapA=[]
lapB=[]
parP=[]
parM=[]
wlist=[]

TparP=[]
TparM=[]
EmidP=[]
EmidM=[]
EendP=[]
EendM=[]

phA_ED=[]
phB_ED=[]
lapA_ED=[]
lapB_ED=[]
parP_ED=[]
parM_ED=[]


TparP_ED=[]
TparM_ED=[]
EmidP_ED=[]
EmidM_ED=[]
EendP_ED=[]
EendM_ED=[]


runtime=[]

"bracket"
def bkt(a,b,c):
    return np.dot(np.conjugate(a),np.dot(b,c))

def dotl(lis):
    dtp=lis[0]
    for i in range(1,len(lis)):
        dtp=np.dot(dtp,lis[i])
    return dtp

"ED wave functions"
psia=copy.deepcopy(yA)
psib=copy.deepcopy(yB)


"DMRG wave functions"
"need to hold ys for level=0 and level=1"
ypt=copy.deepcopy(ypn)
psip=MPS.PsiFromY(ypt)
ymt=copy.deepcopy(ymn)
psim=MPS.PsiFromY(ymt)


"gamma operators"
def gAl(l):
    ntp=1
    for i in range(0,l):
        ntp=np.kron(ntp,sz)
    ntp=np.kron(ntp,sx)
    for i in range(l+1,L):
        ntp=np.kron(ntp,s0)
    return ntp
def gBl(l):
    ntp=1
    for i in range(0,l):
        ntp=np.kron(ntp,sz)
    ntp=np.kron(ntp,1.j*sy)
    for i in range(l+1,L):
        ntp=np.kron(ntp,s0)
    return ntp


gAlist=[]
gBlist=[]
plist=[]
for l in range(0,L):
    gAlist.append(bkt(psim,gAl(l),psip))
    gBlist.append(bkt(psim,gBl(l),psip))
    
    
"Plot the Majorana decomposition"
def plotgammas():
    sites=[]
    for l in range(0,len(ypn)):
        sites.append(l+1)    
    plt.plot(sites,g1A)
    plt.plot(sites,g2A)
    plt.show() 
    
"deffine MBSs"
def gA():
    gtp=0
    for l in range(0,L):
        gtp=gtp+gAlist[l]*gAl(l)
    return gtp

"deffine MBSs"
def gB():
    gtp=0
    for l in range(0,L):
        gtp=gtp+gBlist[l]*gBl(l)
    return gtp


Nt=100
dt=0.01
Vmax=0.1
wait=100
Nw=wait
L=len(ypt)

"Evolution function H(eF(t*dt))"
def eF(t):
    return Vmax*np.sin(t*np.pi/2)


"ED Evolution Operators"
dU=[]
dV=[]
for nt in range(0,Nt):
    dU.append(lng.expm(1j*H(eF(nt*dt))*dt))
    dV.append(lng.expm(-1j*H(eF(nt*dt))*dt)) 
    

"TEBD operators are in Apply_MPO"



"ramp up"
for nt in range(0,Nt):
    ypt=U_MPO.Apply_Uleft(ypt,eF(nt*dt),dt,1)
    ypt=U_MPO.Apply_Uright(ypt,eF(nt*dt),dt,1)
    psip=np.dot(dU[nt],psip)
    psip=np.dot(dU[nt],psip)
    
    ymt=U_MPO.Apply_Uleft(ymt,eF(nt*dt),dt,1)
    ymt=U_MPO.Apply_Uright(ymt,eF(nt*dt),dt,1)
    psim=np.dot(dU[nt],psim)
    psim=np.dot(dU[nt],psim)


psipr=psip
ypr=ypt

"Zap"
mzt=MPO.MPOtoO(oz)
Id=np.identity(len(psip))
mz=(dotl([cl[int(L/2)-1]-dl[int(L/2)-1],cl[int(L/2)]+dl[int(L/2)]]))

mtp=mz-mzt
print(["zap comparison:",np.amax(mtp),np.amin(mtp)])

psipz=psip

ypt=ME.apply_O(oz,ypt)
psip=np.dot(mz,psip)

ymt=ME.apply_O(oz,ymt)
psim=np.dot(mz,psim)

yphold=copy.deepcopy(ypt)
ymhold=copy.deepcopy(ymt)
psiphold=copy.deepcopy(psip)
psimhold=copy.deepcopy(psim)

for Nw in range(0,3000,30):
    a=time.time()
    
    ypt=copy.deepcopy(yphold)
    ymt=copy.deepcopy(ymhold)
    psip=copy.deepcopy(psiphold)
    psim=copy.deepcopy(psimhold)

    "wait"
    for nt in range(0,Nw):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-1)*dt),dt,1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-1)*dt),dt,1)
        psip=np.dot(dU[Nt-1],psip)
        psip=np.dot(dU[Nt-1],psip)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-1)*dt),dt,1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-1)*dt),dt,1)
        psim=np.dot(dU[Nt-1],psim)
        psim=np.dot(dU[Nt-1],psim)
    
    yphold=copy.deepcopy(ypt)
    ymhold=copy.deepcopy(ymt)
    psiphold=copy.deepcopy(psip)
    psimhold=copy.deepcopy(psim)
    
    EmidPw=ME.ME(ypt,MPO_time.HMPO(eF((Nt-1)*dt),L),ypt)
    EmidMw=ME.ME(ymt,MPO_time.HMPO(eF((Nt-1)*dt),L),ymt)
    EmidP.append(EmidPw)
    EmidM.append(EmidMw)
    
    EmidPwED=bkt(psip,H(Vmax),psip)
    EmidMwED=bkt(psim,H(Vmax),psim)
    EmidP_ED.append(EmidPwED)
    EmidM_ED.append(EmidMwED)
    
    
    "ramp down"
    for nt in range(1,Nt+1):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-nt)*dt),dt,-1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-nt)*dt),dt,-1)
        psip=np.dot(dV[Nt-1-nt],psip)
        psip=np.dot(dV[Nt-1-nt],psip)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-nt)*dt),dt,-1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-nt)*dt),dt,-1)
        psim=np.dot(dV[Nt-1-nt],psim)
        psim=np.dot(dV[Nt-1-nt],psim)
        
    psipy=MPS.PsiFromY(ypt)
    psimy=MPS.PsiFromY(ymt)
    
    print('comparisions')    
    print(["comparison even",np.dot(np.conjugate(psip),psipy)])
    print(["comparison odd",np.dot(np.conjugate(psim),psimy)])    
    
    print('error')
    phAw=abs(np.imag(np.log(ME.ME(ymt,gmpo.gxMPO(gxlist,L),ypt))))
    phBw=abs(np.imag(np.log(ME.ME(ymt,gmpo.gyMPO(gylist,L),ypt))))
    lapAw=abs(np.real(np.log(ME.ME(ymt,gmpo.gxMPO(gxlist,L),ypt))))
    lapBw=abs(np.real(np.log(ME.ME(ymt,gmpo.gyMPO(gylist,L),ypt))))
    parPw=ME.ME(ypt,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ypt))
    parMw=ME.ME(ymt,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ymt))
    
    TparPw=ME.ME(ypt,PO.P_MPO(1,L),ypt)
    TparMw=ME.ME(ymt,PO.P_MPO(-1,L),ymt)
    EendPw=ME.ME(ypt,MPO.HMPO(L),ypt)
    EendMw=ME.ME(ymt,MPO.HMPO(L),ymt)
    
    
    phAwED=np.imag(np.log(bkt(psim,gA(),psip)))  
    phBwED=np.imag(np.log(bkt(psim,gB(),psip))) 
    lapAwED=np.real(np.log(bkt(psim,gA(),psip))) 
    lapBwED=np.real(np.log(bkt(psim,gB(),psip))) 
    parMwED=1+np.real(bkt(psim,np.dot(gA(),gB()),psim))  
    parPwED=1-np.real(bkt(psip,np.dot(gA(),gB()),psip))  
 
    
    PpED=MPO.MPOtoO(PO.P_MPO(1,L))
    PmED=MPO.MPOtoO(PO.P_MPO(-1,L))
    HED=MPO.MPOtoO(MPO.HMPO(L))
    TparPwED=bkt(psip,PpED,psip)
    TparMwED=bkt(psim,PmED,psim)
    EendPwED=bkt(psip,HED,psip)
    EendMwED=bkt(psim,HED,psim)

    
    b=time.time()
    
    
    print(["Errors",Nw])
    print(phAw)
    print(phBw)
    print(lapAw)
    print(lapBw)
    print(1-abs(parPw))
    print(1-abs(parMw))
    print("Extra")
    print(TparPw)
    print(TparMw)
    print(EmidPw-EmidMw)
    print(EmidPwED-EmidMwED)
    
    print("time")    
    print((b-a)/60)
    
    
    phA.append(phAw)
    phB.append(phBw)
    lapA.append(lapAw)
    lapB.append(lapBw)
    parP.append(1-abs(parPw))
    parM.append(1-abs(parMw))
    wlist.append(Nw)
    
    TparP.append(TparPw)
    TparM.append(TparMw)
    EendP.append(EendPw)
    EendM.append(EendMw)
    
    phA_ED.append(phAwED)
    phB_ED.append(phBwED)
    lapA_ED.append(lapAwED)
    lapB_ED.append(lapBwED)
    parP_ED.append(1-abs(parPwED))
    parM_ED.append(1-abs(parMwED))
    
    TparP_ED.append(TparPwED)
    TparM_ED.append(TparMwED)
    EendP_ED.append(EendPwED)
    EendM_ED.append(EendMwED)
    
    runtime.append((b-a)/60)    
   

    
    
    
    