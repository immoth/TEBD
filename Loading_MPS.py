# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:51:16 2019

@author: jsten
"""

import pickle

#ypt[2].tofile(file+"test10.txt")


    
with open(file+"mpsP_L"+str(18)+"_W"+str(4500)+"_t"+str(Nt+Nw+Nt)+".txt","rb") as f:
    yptL=pickle.load(f)
with open(file+"mpsM_L"+str(18)+"_W"+str(4500)+"_t"+str(Nt+Nw+Nt)+".txt","rb") as f:
    ymtL=pickle.load(f)
    
    
    phAw=abs(np.imag(np.log(ME.ME(ymtL,gxMPO(gxlist,L),yptL))))
    phBw=abs(np.imag(np.log(ME.ME(ymtL,gyMPO(gylist,L),yptL))))
    lapAw=abs(np.real(np.log(ME.ME(ymtL,gxMPO(gxlist,L),yptL))))
    lapBw=abs(np.real(np.log(ME.ME(ymtL,gyMPO(gylist,L),yptL))))
    parPw=ME.ME(yptL,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),yptL))
    parMw=ME.ME(ymtL,gxMPO(gxlist,L),MPO.apply_O(gyMPO(gylist,L),ymtL))
    
    print(["Errors",wait])
    print(phAw)
    print(phBw)
    print(lapAw)
    print(lapBw)
    print(parPw)
    print(parMw)
    