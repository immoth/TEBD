# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:37:09 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:13:27 2019

@author: jsten
"""

import numpy as np
from cmath import *
import scipy.linalg as lng
import copy
import Matrix_Element as ME 
import MPS
import MPO

"only works for 0<l<L-1"
def optimize(Mps,l,level):
    mtp=copy.deepcopy(Mps)
    dd=len(mtp[0])
    L=len(mtp)
    DD=len(mtp[l][0])
    DDp=len(mtp[l][0][0])
    h=MPO.HMPO(L)
    hh=ME.dME(mtp,h,mtp,l)
    ss=MPS.dIN(mtp,mtp,l)
    ht=(hh+np.transpose(hh))/2  
    st=(ss+np.transpose(ss))/2
    "egn=lng.eig(ht,st)"
    egn=lng.eig(ht)
    et=egn[0]
    ev=np.transpose(egn[1])
    
    srt=np.argsort(et)
    rtp=np.reshape(ev[srt[level]],(dd,DD,DDp)) #change srt[n] to adjust energy level 
    mtp[l]=rtp
    return MPS.nMPS(mtp)

"""
Mps=y
l=3
mtp=copy.deepcopy(Mps)
dd=len(mtp[0])
L=len(mtp)
DD=len(mtp[l][0])
DDp=len(mtp[l][0][0])
h=MPO.HMPO(L)
hh=ME.dME(mtp,h,mtp,l)
ss=MPS.dIN(mtp,mtp,l)
ht=(hh+np.transpose(hh))/2  
st=(ss+np.transpose(ss))/2
egn=lng.eig(ht,st)
"egn=lng.eig(ht)"
et=egn[0]
ev=np.transpose(egn[1])

mini=np.argmin(et)
rtp=np.reshape(ev[mini],(dd,DD,DDp))
mtp[l]=rtp
yn=MPS.nMPS(mtp)
  
print(bkt(np.conjugate(ev[mini]),ht,ev[mini])/bkt(np.conjugate(ev[mini]),st,ev[mini]))   
print(ME.ME(mtp,h,mtp)/bkt(np.conjugate(ev[mini]),st,ev[mini]))
print(ME.ME(yn,h,yn))
print(et[mini])
"""


"""
print("Optimize")
print(opo.Opt(y,3)[1][1][0][0])
print(Opt4(y,3)[1][1][0][0])
"""

