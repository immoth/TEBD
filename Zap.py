# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:36:11 2019

@author: jsten
"""

import numpy as np
import MPS


"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
I2=np.dot(sz,sz)
Z2=sz-sz


def gx(k,L):
    if k==0:
        ztp=[np.array([Z2,sx])]
    else:
        ztp=[np.array([Z2,sz])]
    
    for l in range(1,k):
        ztp.append(np.array([[Z2,Z2],[Z2,sz]]))
    
    if k==L-1:
        ztp.append(np.array([Z2,sx]))
    elif k==0:
        for l in range(k+1,L-1):
            ztp.append(np.array([[Z2,Z2],[Z2,s0]]))
        
        ztp.append(np.array([Z2,s0]))
    else:
        ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
        
        for l in range(k+1,L-1):
            ztp.append(np.array([[Z2,Z2],[Z2,s0]]))
        
        ztp.append(np.array([Z2,s0]))
    
    return ztp


def gy(k,L):
    if k==0:
        ztp=[np.array([Z2,sy])]
    else:
        ztp=[np.array([Z2,sz])]
    
    for l in range(1,k):
        ztp.append(np.array([[Z2,Z2],[Z2,sz]]))
    
    if k==L-1:
        ztp.append(np.array([Z2,sy]))
    elif k==0:
        for l in range(k+1,L-1):
            ztp.append(np.array([[Z2,Z2],[Z2,s0]]))
        
        ztp.append(np.array([Z2,s0]))
    else:
        ztp.append(np.array([[Z2,Z2],[Z2,sy]]))
        
        for l in range(k+1,L-1):
            ztp.append(np.array([[Z2,Z2],[Z2,s0]]))
        
        ztp.append(np.array([Z2,s0]))
    
    return ztp



def zap(n1,n2,L):

    ztp=[np.array([Z2,I2])]
    
    for l in range(1,n1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
    
    for l in range(n1+1,n2):
        ztp.append(np.array([[Z2,Z2],[Z2,sz]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
        
    for l in range(n2+1,L-1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([Z2,I2]))
    
    return ztp

def zapN(n1,n2,L):

    ztp=[np.array([Z2,I2])]
    
    for l in range(1,n1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
    
    for l in range(n1+1,n2):
        ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx]]))
        
    for l in range(n2+1,L-1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([Z2,I2]))
    
    return ztp


def zapR(n1,n2,L):

    ztp=[np.array([Z2,I2])]
    
    for l in range(1,n1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,I2+sx]]))
    
    for l in range(n1+1,n2):
        ztp.append(np.array([[Z2,Z2],[Z2,I2+sx]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,I2+sx]]))
        
    for l in range(n2+1,L-1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([Z2,I2]))
    
    return ztp


def zapNc(n1,n2,L):

    ztp=[np.array([Z2,I2])]
    
    for l in range(1,n1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx+1j*sy]]))
    
    for l in range(n1+1,n2):
        ztp.append(np.array([[Z2,Z2],[Z2,sx+1j*sy]]))
        
    ztp.append(np.array([[Z2,Z2],[Z2,sx+1j*sy]]))
        
    for l in range(n2+1,L-1):
        ztp.append(np.array([[Z2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([Z2,I2]))
    
    return ztp

def zapB2(n1,n2,L):

    ztp=[np.array([1/np.sqrt(2)*I2,1/np.sqrt(2)*I2])]
    
    for l in range(1,n1):
        ztp.append(np.array([[I2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([[sy,Z2],[Z2,sx]]))
    
    for l in range(n1+1,n2):
        ztp.append(np.array([[I2,Z2],[Z2,sz]]))
        
    ztp.append(np.array([[sy,Z2],[Z2,sx]]))
        
    for l in range(n2+1,L-1):
        ztp.append(np.array([[I2,Z2],[Z2,I2]]))
        
    ztp.append(np.array([I2,I2]))
    
    return ztp


















