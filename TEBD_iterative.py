# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:12:16 2019

@author: jsten
"""
import pickle

import Matrix_Element as ME
import MPO
import copy
import U_MPO
import Zap

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
    gxlist.append((-1)**(L-1)*ME.ME(ymn,gxlMPO(l,L),ypn))
    gylist.append((-1)**(L-1)*ME.ME(ymn,gylMPO(L-1-l,L),ypn))
"there is some (-1)**(L-1) in gxlMPO and gylMPO that shouldn't be there"
        
print(ME.ME(ymn,gxMPO(gxlist,L),ypn))
print(ME.ME(ymn,gyMPO(gylist,L),ypn))
print(ME.ME(ypn,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),ypn)))
print(ME.ME(ymn,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),ymn)))

"Now I just need to copy TEBD from TEBD_and_ED"

Nt=100
dt=0.01
Vmax=0.1
#wait=3000
#Nw=wait
L=len(ypt)

"Evolution function H(eF(t*dt))"
def eF(t):
    return Vmax*np.sin(t*np.pi/2)

phA=[]
phB=[]
lapA=[]
lapB=[]
parP=[]
parM=[]
wlist=[]
file='C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_functions_BondControl\\mps data\\'
for wait in range(0,1000,50):
    
    "DMRG wave functions"
    ypt=copy.deepcopy(ypn)
    ymt=copy.deepcopy(ymn)
    Nw=wait
    
    
    "ramp up"
    for nt in range(0,Nt):
        ypt=U_MPO.Apply_Uleft(ypt,eF(nt*dt),dt,1)
        ypt=U_MPO.Apply_Uright(ypt,eF(nt*dt),dt,1)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF(nt*dt),dt,1)
        ymt=U_MPO.Apply_Uright(ymt,eF(nt*dt),dt,1)
        
        
    print("ramped up")     
      
    "Zap"
    oz=Zap.zap(int(L/2)-1,int(L/2),L)
    ypt=ME.apply_O(oz,ypt)
    ymt=ME.apply_O(oz,ymt)
    
    
    
    "wait"
    for nt in range(0,Nw):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-1)*dt),dt,1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-1)*dt),dt,1)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-1)*dt),dt,1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-1)*dt),dt,1)
        
    
        
    "ramp down"
    for nt in range(1,Nt+1):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-nt)*dt),dt,-1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-nt)*dt),dt,-1)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-nt)*dt),dt,-1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-nt)*dt),dt,-1)
        
        
    print("ramped down")
    
    phAw=abs(np.imag(np.log(ME.ME(ymt,gxMPO(gxlist,L),ypt))))
    phBw=abs(np.imag(np.log(ME.ME(ymt,gyMPO(gylist,L),ypt))))
    lapAw=abs(np.real(np.log(ME.ME(ymt,gxMPO(gxlist,L),ypt))))
    lapBw=abs(np.real(np.log(ME.ME(ymt,gyMPO(gylist,L),ypt))))
    parPw=ME.ME(ypt,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),ypt))
    parMw=ME.ME(ymt,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),ymt))
    
    print(["Errors",wait])
    print(phAw)
    print(phBw)
    print(lapAw)
    print(lapBw)
    print(parPw)
    print(parMw)
    
    phA.append(phAw)
    phB.append(phBw)
    lapA.append(lapAw)
    lapB.append(lapBw)
    parP.append(1-abs(parPw))
    parM.append(1-abs(parMw))
    wlist.append(wait)




















