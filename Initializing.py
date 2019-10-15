# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:49:01 2019

@author: jsten
"""

import DMRG
import MPS
import Parity_Operator as PO
import Matrix_Element as ME
import Hamiltonian_DE as HDE

L=5
DD=7
dd=2

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

psia=HDE.yA
psib=HDE.yB

psip=MPS.PsiFromY(ypn)
psim=MPS.PsiFromY(ymn)

"""
print("Compair to DE")
print(np.dot(np.conjugate(psip),psib))
print(np.dot(np.conjugate(psim),psia))
"""
