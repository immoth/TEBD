# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:57:34 2019

@author: jsten
"""
import numpy as np

"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
z=s0-s0
sp=1/2*(sx+1j*sy)
sm=1/2*(sx-1j*sy)


def gxlMPO(l,L):
    gtp=[]
    if l==0:
        gtp.append(np.array([sx,z]))
    else:
        gtp.append(np.array([sz,z]))
    for k in range(1,l):
        gtp.append(np.array([[sz,z],[z,z]]))
    if l!=0 and l!=L-1:
        gtp.append(np.array([[sx,z],[z,z]]))
    for k in range(l+1,L-1):
        gtp.append(np.array([[s0,z],[z,z]]))
    if l==L-1:
        gtp.append(np.array([sx,z]))
    else:
        gtp.append(np.array([s0,z]))
    gtp.reverse()
    return gtp

def gylMPO(l,L):
    gtp=[]
    if l==0:
        gtp.append(np.array([1j*sy,z]))
    else:
        gtp.append(np.array([sz,z]))
    for k in range(1,l):
        gtp.append(np.array([[sz,z],[z,z]]))
    if l!=0 and l!=L-1:
        gtp.append(np.array([[1j*sy,z],[z,z]]))
    for k in range(l+1,L-1):
        gtp.append(np.array([[s0,z],[z,z]]))
    if l==L-1:
        gtp.append(np.array([1j*sy,z]))
    else:
        gtp.append(np.array([s0,z]))
    gtp.reverse()
    return gtp


def gxMPO(wl,L):
    d=len(wl)
    Vl=[wl[0]*sx]
    for dd in range(1,d):
        Vl.append(wl[dd]*sz)
    Vl=np.array(Vl)
    gtp=[Vl]
    for l in range(1,L-1):
        mtp=np.array([[z]*d]*d)
        for dd in range(0,d):
            if dd<l:
                mtp[dd,dd]=s0
            elif dd==l:
                mtp[dd,dd]=sx
            else:
                mtp[dd,dd]=sz
        gtp.append(np.array(mtp))
    Vr=np.array([s0]*d)
    if L-1<=d-1:
        Vr[L-1]=sx
    gtp.append(Vr)
    return gtp

def gyMPO(wl,L):
    d=len(wl)
    Vl=[wl[0]*1j*sy]
    for dd in range(1,d):
        Vl.append(wl[dd]*s0)
    Vl=np.array(Vl)
    gtp=[Vl]
    for l in range(1,L-1):
        mtp=np.array([[z]*d]*d)
        for dd in range(0,d):
            if dd<l:
                mtp[dd,dd]=sz
            elif dd==l:
                mtp[dd,dd]=1j*sy
            else:
                mtp[dd,dd]=s0
        gtp.append(np.array(mtp))
    Vr=np.array([sz]*d)
    if L-1<=d-1:
        Vr[L-1]=1j*sy
    gtp.append(Vr)
    gtp.reverse()
    return gtp 

"""
def gxMPO(wl,L):
    d=len(wl)
    Vl=[wl[d-1]*sx]
    for dd in range(1,d):
        Vl.append(wl[d-dd-1]*s0)
    Vl=np.array(Vl)
    gtp=[Vl]
    for l in range(1,L-1):
        mtp=np.array([[z]*d]*d)
        for dd in range(0,d):
            if dd<l:
                mtp[dd,dd]=sz
            elif dd==l:
                mtp[dd,dd]=sx
            else:
                mtp[dd,dd]=s0
        gtp.append(np.array(mtp))
    Vr=np.array([sz]*d)
    if L-1<=d-1:
        Vr[L-1]=sx
    gtp.append(Vr)
    return gtp


def gyMPO(wl,L):
    d=len(wl)
    Vl=[wl[d-1]*1j*sy]
    for dd in range(1,d):
        Vl.append(wl[d-dd-1]*s0)
    Vl=np.array(Vl)
    gtp=[Vl]
    for l in range(1,L-1):
        mtp=np.array([[z]*d]*d)
        for dd in range(0,d):
            if dd<l:
                mtp[dd,dd]=sz
            elif dd==l:
                mtp[dd,dd]=1j*sy
            else:
                mtp[dd,dd]=s0
        gtp.append(np.array(mtp))
    Vr=np.array([sz]*d)
    Vr[d-1]=1j*sy
    gtp.append(Vr)
    return gtp   
        
"""        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        