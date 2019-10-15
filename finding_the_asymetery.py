# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:44:03 2019

@author: jsten
"""

import copy
import numpy as np
import MPS
import scipy.linalg as lng
import H_time
import U_MPO
import U_MPO_old
import U_MPO_new
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
ypto=copy.deepcopy(ypn)
psip=MPS.PsiFromY(ypt)
ymt=copy.deepcopy(ymn)
ymto=copy.deepcopy(ymn)
psim=MPS.PsiFromY(ymt)


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
    ypt=U_MPO_new.Apply_Uleft(ypt,eF(nt*dt),dt,1)
    ypt=U_MPO_new.Apply_Uright(ypt,eF(nt*dt),dt,1)
    ypto=U_MPO_old.Apply_Uleft(ypto,eF(nt*dt),1)
    ypto=U_MPO_old.Apply_Uright(ypto,eF(nt*dt),1)
    psip=np.dot(dU[nt],psip)
    psip=np.dot(dU[nt],psip)
    
    ymt=U_MPO_new.Apply_Uleft(ymt,eF(nt*dt),dt,1)
    ymt=U_MPO_new.Apply_Uright(ymt,eF(nt*dt),dt,1)
    ymto=U_MPO_old.Apply_Uleft(ymto,eF(nt*dt),1)
    ymto=U_MPO_old.Apply_Uright(ymto,eF(nt*dt),1)
    psim=np.dot(dU[nt],psim)
    psim=np.dot(dU[nt],psim)
    
    
psipy=MPS.PsiFromY(ypt)
psimy=MPS.PsiFromY(ymt)
psipoy=MPS.PsiFromY(ypto)
psimoy=MPS.PsiFromY(ymto)


print(np.dot(np.conjugate(psipy),psip))
print(np.dot(np.conjugate(psimy),psim))
print(np.dot(np.conjugate(psipoy),psip))
print(np.dot(np.conjugate(psimoy),psim))






