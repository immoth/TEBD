# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:49:01 2019

@author: jsten
"""

import DMRG
import MPS
import Parity_Operator as PO
import Matrix_Element as ME
import Canonical_Form as CanF
import numpy as np
import Zap

"Parameters"
tua=1;
Delta=0.7;
U=0.0;
mu=0.2;

params=np.array([tua,Delta,U,mu])
np.savetxt("params",params)

"Sizes"
L=16
DD=3
dd=2

"Zap opperator"
n1=int(L/2)-1
n2=int(L/2)
oz=Zap.zapN(n1,n2,L)

y=DMRG.DMRG(L,DD,dd,0)

op=PO.P_MPO(1,L)
om=PO.P_MPO(-1,L)

yp=ME.apply_O(op,y)
ypn=MPS.nMPS(yp)

ym=ME.apply_O(om,y)
ymn=MPS.nMPS(ym)

print("without level 1")
print(ME.ME(ypn,op,ypn))
print(ME.ME(ymn,om,ymn))

if abs(ME.ME(ypn,op,ypn)-1)>10**(-8):
    ypn=DMRG.DMRG(L,DD,dd,1)
    
if abs(ME.ME(ymn,om,ymn)-1)>10**(-8):
    ymn=DMRG.DMRG(L,DD,dd,1)
    
print("with level 1")
print(ME.ME(ypn,op,ypn))
print(ME.ME(ymn,om,ymn))

for l in range(1,L):
    ypn=CanF.LCon(ypn,L-l)
    ymn=CanF.LCon(ymn,L-l)
    
print("after canonicalization")
print(ME.ME(ypn,op,ypn))
print(ME.ME(ymn,om,ymn))


