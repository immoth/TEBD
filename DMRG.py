# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:46:34 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:24:09 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt
from cmath import *
import scipy.linalg as lng

import MPS
import Canonical_Form as CanF
import Optimize
import Matrix_Element as ME
import MPO
import Parity_Operator as PO

def DMRG(L,DD,dd,level):
    x=MPS.MPS(L,DD,dd)
    y=MPS.nMPS(x)
    
    # print(MPS.innerMPS(y,y))
    dd=len(y[0])
    L=len(y)
    DD=len(y[0][0])
    h=MPO.HMPO(L)
    
    
    
    eplt=[]
    yT=[]
    "end vectors blow up for MPS(5,3,2)"
    "I think im doing LCon from the wrong direction"
    for t in range(0,6):
        y=CanF.RCon(y,0)
        yT.append(y)
        for l in range(1,L-1):
            y=CanF.LCon(y,L-l)
        for l in range(1,L-1):
            y=Optimize.optimize(y,l,level)
            yT.append(y)
            etmp=ME.ME(y,h,y)
            eplt.append(etmp)
            #print([t,l,etmp])
            y=CanF.RCon(y,l)
            yT.append(y)
    return y      


"""    
# plt.plot(eplt)
# plt.show()



op=PO.P_MPO(1,L)
om=PO.P_MPO(-1,L)

# print(ME.ME(y,op,y))
# print(ME.ME(y,om,y))


yp=ME.apply_O(op,y)
ypn=MPS.nMPS(yp)
#print(ME.ME(ypn,h,ypn))
#print(ME.ME(ypn,op,ypn))

ym=ME.apply_O(om,y)
ymn=MPS.nMPS(ym)
#print(ME.ME(ymn,h,ymn))
#print(ME.ME(ymn,om,ymn))
"""






"""
"To test if it is an eigenvalue"
max(MPS.PsiFromY(ME.apply_O(h,ymn))/ME.ME(ymn,h,ymn)-MPS.PsiFromY(ymn))
"""







