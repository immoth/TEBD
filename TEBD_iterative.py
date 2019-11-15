# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:12:16 2019

@author: jsten
"""
import pickle
import numpy as np
import copy

import Matrix_Element as ME
import MPO
import U_MPO
import Zap
import GammaL_MPO as gmpo
import Parity_Operator as PO
import MPO_time


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

BD=40 #must be changed in U_MPO
Nt=500
dt=0.01
Vmax=0.1
#wait=3000
#Nw=wait
L=len(ypt)

"Evolution function H(eF(t*dt))"
ramp=1/(Nt*dt)
def eF(t):
    return Vmax*np.sin(ramp*t*np.pi/2)

phA=[]
phB=[]
lapA=[]
lapB=[]
parP=[]
parM=[]
wlist=[]
file='C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_functions_BondControl\\mps data\\'

TparP=[]
TparM=[]
EmidP=[]
EmidM=[]
EendP=[]
EendM=[]
    
"DMRG wave functions"
ypt=copy.deepcopy(ypn)
ymt=copy.deepcopy(ymn)

"ramp up"
for nt in range(0,Nt):
    ypt=U_MPO.Apply_Uleft(ypt,eF(nt*dt),dt,1)
    ypt=U_MPO.Apply_Uright(ypt,eF(nt*dt),dt,1)
    
    ymt=U_MPO.Apply_Uleft(ymt,eF(nt*dt),dt,1)
    ymt=U_MPO.Apply_Uright(ymt,eF(nt*dt),dt,1)
    
    
print("ramped up")     


"Zap"
ypt=ME.apply_O(oz,ypt)
ymt=ME.apply_O(oz,ymt)

yphold=copy.deepcopy(ypt)
ymhold=copy.deepcopy(ymt)

Nw0=0
    
for wait in range(0,3000,30):  
    Nw=wait
    ypt=copy.deepcopy(yphold)
    ymt=copy.deepcopy(ymhold)
    
    "wait"
    for nt in range(Nw0,Nw):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-1)*dt),dt,1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-1)*dt),dt,1)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-1)*dt),dt,1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-1)*dt),dt,1)
        
    Nw0=Nw
    yphold=copy.deepcopy(ypt)
    ymhold=copy.deepcopy(ymt)
    
    EmidPw=ME.ME(ypt,MPO_time.HMPO(eF((Nt-1)*dt),L),ypt)
    EmidMw=ME.ME(ymt,MPO_time.HMPO(eF((Nt-1)*dt),L),ymt)
    
    EmidP.append(EmidPw)
    EmidM.append(EmidMw)
        
    "ramp down"
    for nt in range(1,Nt+1):
        ypt=U_MPO.Apply_Uleft(ypt,eF((Nt-nt)*dt),dt,-1)
        ypt=U_MPO.Apply_Uright(ypt,eF((Nt-nt)*dt),dt,-1)
        
        ymt=U_MPO.Apply_Uleft(ymt,eF((Nt-nt)*dt),dt,-1)
        ymt=U_MPO.Apply_Uright(ymt,eF((Nt-nt)*dt),dt,-1)
        
        
    print("ramped down")
    
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
    
    print(["Errors",wait])
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
    print(EendPw-EendMw)
    
    phA.append(phAw)
    phB.append(phBw)
    lapA.append(lapAw)
    lapB.append(lapBw)
    parP.append(1-abs(parPw))
    parM.append(1-abs(parMw))
    wlist.append(wait)
    
    TparP.append(TparPw)
    TparM.append(TparMw)
    EendP.append(EendPw)
    EendM.append(EendMw)
    
    filename=str(mu)+"_J"+str(tua)+"_D"+str(Delta)+"_V"+str(Vmax)+"_L"+str(L)+"_tr"+str(Nt)+"_tw"+str('F')+"_dt"+str(dt)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alpha)
    
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_phA"+".txt","wb") as f:
        pickle.dump(phA,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_phB"+".txt","wb") as f:
        pickle.dump(phB,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_lapA"+".txt","wb") as f:
        pickle.dump(lapA,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_lapB"+".txt","wb") as f:
        pickle.dump(lapB,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_parP"+".txt","wb") as f:
        pickle.dump(parP,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_parM"+".txt","wb") as f:
        pickle.dump(parM,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_wlist"+".txt","wb") as f:
        pickle.dump(wlist,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_TparP"+".txt","wb") as f:
        pickle.dump(TparP,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_TparM"+".txt","wb") as f:
        pickle.dump(TparM,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_EendP"+".txt","wb") as f:
        pickle.dump(EendP,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_EendM"+".txt","wb") as f:
        pickle.dump(EendM,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_EmidP"+".txt","wb") as f:
        pickle.dump(EmidP,f)
    with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_clean\data_std\_m"+filename+"_EmidM"+".txt","wb") as f:
        pickle.dump(EmidM,f)



















