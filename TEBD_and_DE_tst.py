# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 10:03:07 2019

@author: jsten
"""

import copy
import numpy as np
import MPS
import scipy.linalg as lng
#import H_time
import U_MPO
import MPO
import Matrix_Element as ME
import Zap

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

ypAA=ypt

psipr=psip
ypr=ypt

"Zap"
oz=Zap.zap(int(L/2)-1,int(L/2),L)
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

psipw=psip
    
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
print(["gA",bkt(psimy,gA(),psipy)])
print(["gB",bkt(psimy,gB(),psipy)])
print(["phase",np.imag(np.log(bkt(psimy,gA(),psipy)))])    
print(["overlap",np.real(np.log(bkt(psimy,gA(),psipy)))])  
print(["phase ED",np.imag(np.log(bkt(psim,gA(),psip)))])    
print(["overlap ED",np.real(np.log(bkt(psim,gA(),psip)))]) 
print(["parity",1+np.real(bkt(psimy,np.dot(gA(),gB()),psimy))])   
print(["parity",1-np.real(bkt(psipy,np.dot(gA(),gB()),psipy))])  
print(["parityED",1+np.real(bkt(psim,np.dot(gA(),gB()),psim))])   
print(["parityED",1-np.real(bkt(psip,np.dot(gA(),gB()),psip))])     
   
""" 
wlist.append(wait)
phE.append(abs(np.imag(np.log(bkt(psimy,gA(),psipy)))))  
flE.append(abs(np.real(np.log(bkt(psimy,gA(),psipy)))))    
phED.append(abs(np.imag(np.log(bkt(psim,gA(),psip)))))  
flED.append(abs(np.real(np.log(bkt(psim,gA(),psip)))))    
pmE.append(1+np.real(bkt(psimy,np.dot(gA(),gB()),psimy)))      
pmED.append(1+np.real(bkt(psim,np.dot(gA(),gB()),psim))) 
ppE.append(1-np.real(bkt(psipy,np.dot(gA(),gB()),psipy)))  
ppED.append(1-np.real(bkt(psip,np.dot(gA(),gB()),psip)))  
"""    
    
    
"""
wlist=[]
flE=[]
phE=[]
flED=[]
phED=[]
ppE=[]
ppED=[]
pmE=[]
pmED=[]
"""    
    
    
    
    