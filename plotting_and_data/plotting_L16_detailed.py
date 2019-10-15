# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt

phAL=np.loadtxt("zzz_phA_L16_d10")
phBL=np.loadtxt("zzz_phB_L16_d10")
lapAL=np.loadtxt("zzz_lapA_L16_d10")
lapBL=np.loadtxt("zzz_lapB_L16_d10")
parPL=np.loadtxt("zzz_parA_L16_d10")
parML=np.loadtxt("zzz_parB_L16_d10")
wlistL=np.loadtxt("zzz_wlist_d16")

plt.figure("Phase Error")
plt.scatter(wlistL,phAL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()

plt.figure("Parity Error")
plt.scatter(wlistL,parPL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.show()
