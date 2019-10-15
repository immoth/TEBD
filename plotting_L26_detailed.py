# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np


np.savetxt("zzz_phA_L26_d10",phA)
np.savetxt("zzz_phB_L26_d10",phB)
np.savetxt("zzz_lapA_L26_d10",lapA)
np.savetxt("zzz_lapB_L26_d10",lapB)
np.savetxt("zzz_parA_L26_d10",parP)
np.savetxt("zzz_parB_L26_d10",parM)
np.savetxt("zzz_wlist_d26",wlist)

phAL=np.loadtxt("zzz_phA_L26_d10")
phBL=np.loadtxt("zzz_phB_L26_d10")
lapAL=np.loadtxt("zzz_lapA_L26_d10")
lapBL=np.loadtxt("zzz_lapB_L26_d10")
parPL=np.loadtxt("zzz_parA_L26_d10")
parML=np.loadtxt("zzz_parB_L26_d10")
wlistL=np.loadtxt("zzz_wlist_d26")

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

plt.figure("Lap Error")
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Lap Error")
plt.show()
