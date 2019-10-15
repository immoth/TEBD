# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:54:30 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:50:10 2019

@author: jsten
"""

import numpy as np
import numpy.linalg as lng
import matplotlib.pyplot as plt
import sys
import copy

np.set_printoptions(threshold=sys.maxsize)

def C(M):
    return np.conj(M)

"""
"Parameters"
Nx=5;
Delta=0.7;
t=1.0;
mu=0.2;
V=0.0;
"""


"Get parameters from the initilization file"
Nx=L
params=np.loadtxt("params")
t=params[0]
Delta=params[1]
V=params[2]
mu=params[3]


"Spin Matrices"
s0=np.array([[1,0],[0,1]])
sx=np.array([[0,1],[1,0]])
sy=np.array([[0,1j],[-1j,0]])
sz=np.array([[1,0],[0,-1]])
z=s0-s0
sp=1/2*(sx+1j*sy)
sm=1/2*(sx-1j*sy)

"Kronecker Product for arbitarty number of matrices"
def krn(lis):
    lis_L=len(lis)
    ktp=lis[0]
    for l in range(1,lis_L):
        ktp=np.kron(lis[l],ktp)
    return ktp

"creats lists to be inserted into krn"
cL=np.zeros([Nx,Nx,2,2],dtype=np.complex_)
dL=np.zeros([Nx,Nx,2,2],dtype=np.complex_)
for l in range(0,Nx):
    cL[l,l]=sp
    dL[l,l]=sm
    for ll in range(0,l):
        cL[l,ll]=sz
        dL[l,ll]=sz
    for ll in range(l+1,Nx):
        cL[l,ll]=s0
        dL[l,ll]=s0

"creation and destruction operators"
cl=[]
dl=[]
for l in range(0,Nx):
    cl.append(krn(cL[l]))
    dl.append(krn(dL[l]))

"Local Hamiltonian h(i)"
def h(i,V):
    if(i<Nx-1):
        Dtp=Delta*(np.dot(cl[i],cl[i+1])+np.dot(dl[i+1],dl[i]))
        Ttp=t*(np.dot(cl[i],dl[i+1])+np.dot(cl[i+1],dl[i]))
        Mtp=mu*(np.dot(cl[i],dl[i])-np.dot(dl[i],cl[i]))
        Utp=V*(np.dot(np.dot(cl[i],dl[i])-np.dot(dl[i],cl[i]),np.dot(cl[i+1],dl[i+1])-np.dot(dl[i+1],cl[i+1])))
        htp=Dtp+Ttp+Mtp+Utp
    else:
        Mtp=mu*(np.dot(cl[i],dl[i])-np.dot(dl[i],cl[i]))
        htp=Mtp
    return htp

"Total Hamiltonian H"
def H(V):
    http=h(0,V)
    for l in range(1,Nx):
        http=http+h(l,V)
    return http

"Eigenvalues"
egn=lng.eig(H(V))
order=np.argsort(egn[0])
el=[]
yl=[]
for n in range(0,len(order)):
    el.append(egn[0][order[n]])
    yl.append(egn[1][:,order[n]])

"""    
"Plotting Energy"
idx=[]
for n in range(0,len(order)):
    idx.append(n)
plt.plot(idx,el,'ro')
plt.show()
"""


"Majorana operators"
g1=[]
g2=[]
g1A=[]
g2A=[]
l0=0
l1=1
for l in range(0,Nx):
    A1=np.dot(yl[l1],np.dot(cl[l]+dl[l],yl[l0]))
    A2=np.dot(yl[l1],np.dot(cl[l]-dl[l],yl[l0]))
    g1A.append(A1)
    g2A.append(A2)
    g1.append(A1*(cl[l]+dl[l]))
    g2.append(A2*(cl[l]-dl[l]))

"""
"Plot the Majorana decomposition"
sites=[]
for l in range(0,Nx):
    sites.append(l+1)
    
plt.plot(sites,g1A)
plt.plot(sites,g2A)
plt.show()
"""

"seperates even and odd ground states"
c=yl[0][0]/yl[1][0]
b=yl[0][1]/yl[1][1]
yA=copy.deepcopy(yl[0]-c*yl[1])
yB=copy.deepcopy(yl[0]-b*yl[1])
yA=yA/np.sqrt(np.dot(yA,yA))
yB=yB/np.sqrt(np.dot(yB,yB))