# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:16:21 2019

@author: jsten
"""

import numpy as np

"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
I2=np.dot(sz,sz)
Z2=sz-sz

Vxl=np.array([sx,Z2])
Mx=np.array([[s0,Z2],[Z2,Z2]])
Vxr=np.array([s0,Z2])

Vyl=np.array([sz,Z2])
My=np.array([[sz,Z2],[Z2,Z2]])
Vyr=np.array([sy,Z2])

def gxMPO(L):
    gtp=[Vxl]
    for i in range(1,L-1):
        gtp.append(Mx)
    gtp.append(Vxr)
    return gtp
    
def gyMPO(L):
    gtp=[Vyl]
    for i in range(1,L-1):
        gtp.append(My)
    gtp.append(Vyr)
    return gtp
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    