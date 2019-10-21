# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:12:16 2019

@author: jsten
"""
import numpy as np

import Matrix_Element as ME
import MPO
import copy
import U_MPO
import Zap
import Canonical_Form as CanF
import GammaL_MPO as gmpo
import Parity_and_Entropy as PaE
import MPS

import time


a=time.time()

"DMRG wave functions"
ypt=copy.deepcopy(ypn)
ymt=copy.deepcopy(ymn)

print("MPS defined")

L=len(ypt)
gxlist=[]
gylist=[]
plist=[]
cut=4
for l in range(0,cut):
    gxlist.append((-1)**(L-1)*ME.ME(ymn,gmpo.gxlMPO(l,L),ypn))
    gylist.append((-1)**(L-1)*ME.ME(ymn,gmpo.gylMPO(L-1-l,L),ypn))
"there is some (-1)**(L-1) in gxlMPO and gylMPO that shouldn't be there"
        
print(ME.ME(ymn,gmpo.gxMPO(gxlist,L),ypn))
print(ME.ME(ymn,gmpo.gyMPO(gylist,L),ypn))
print(ME.ME(ypn,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ypn)))
print(ME.ME(ymn,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ymn)))

"Now I just need to copy TEBD from TEBD_and_ED"

Nt=100
dt=0.01
Vmax=1.0
wait=2000
Nw=wait
ramp=1.0
L=len(ypt)

"Evolution function H(eF(t*dt))"
def eF(t):
    return Vmax*np.sin(ramp*t*np.pi/2)

eplist=[]
pplist=[]
emlist=[]
pmlist=[]

"ramp up"
for nt in range(0,Nt):
    ypt=U_MPO.Apply_Uleft(ypt,eF(nt*dt),dt,1)
    ypt=U_MPO.Apply_Uright(ypt,eF(nt*dt),dt,1)
    
    ymt=U_MPO.Apply_Uleft(ymt,eF(nt*dt),dt,1)
    ymt=U_MPO.Apply_Uright(ymt,eF(nt*dt),dt,1)
    
    """
    eplist.append(PaE.entL(ypt))
    emlist.append(PaE.entL(ymt))
    pplist.append(PaE.parL(ypt))
    pmlist.append(PaE.parL(ymt))
    """
    
print("ramped up")     


ypr=copy.deepcopy(ypt)
ymr=copy.deepcopy(ymt)


"Zap"
ypt=ME.apply_O(oz,ypt)
ymt=ME.apply_O(oz,ymt)

ypt=MPS.nMPS(ypt)
ymt=MPS.nMPS(ymt)

ypt=CanF.LConAll(ypt)
ymt=CanF.LConAll(ymt)

ypz=copy.deepcopy(ypt)
ymz=copy.deepcopy(ymt)
print("zapped")



"wait"
for nt in range(0,Nw):
    ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-1)*dt),dt,1)
    ypt=U_MPO.Apply_Uright(ypt,eF((Nt-1)*dt),dt,1)
    
    ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-1)*dt),dt,1)
    ymt=U_MPO.Apply_Uright(ymt,eF((Nt-1)*dt),dt,1)
    
    """
    eplist.append(PaE.entL(ypt))
    emlist.append(PaE.entL(ymt))
    pplist.append(PaE.parL(ypt))
    pmlist.append(PaE.parL(ymt))
    """

print("waited")
    
"ramp down"
for nt in range(1,Nt+1):
    ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-nt)*dt),dt,-1)
    ypt=U_MPO.Apply_Uright(ypt,eF((Nt-nt)*dt),dt,-1)
    
    ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-nt)*dt),dt,-1)
    ymt=U_MPO.Apply_Uright(ymt,eF((Nt-nt)*dt),dt,-1)
    
    """
    eplist.append(PaE.entL(ypt))
    emlist.append(PaE.entL(ymt))
    pplist.append(PaE.parL(ypt))
    pmlist.append(PaE.parL(ymt))
    """

print("ramped down")

print("Errors")
phAd=np.imag(np.log(ME.ME(ymt,gmpo.gxMPO(gxlist,L),ypt)))
phBd=np.imag(np.log(ME.ME(ymt,gmpo.gyMPO(gxlist,L),ypt)))
lapAd=np.real(np.log(ME.ME(ymt,gmpo.gxMPO(gxlist,L),ypt)))
lapBd=np.real(np.log(ME.ME(ymt,gmpo.gyMPO(gxlist,L),ypt)))
parAd=1-abs(ME.ME(ypt,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ypt)))
parBd=1-abs(ME.ME(ymt,gmpo.gxMPO(gxlist,L),MPO.apply_O(gmpo.gyMPO(gylist,L),ymt)))

print(phAd)
print(phBd)
print(lapAd)
print(lapBd)
print(parAd)
print(parBd)

b=time.time()

print((b-a)/60)


















