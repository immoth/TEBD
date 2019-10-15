# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np
"""
np.savetxt("zzz_phA_L16_d10_N10",phA)
np.savetxt("zzz_phB_L16_d10_N10",phB)
np.savetxt("zzz_lapA_L16_d10_N10",lapA)
np.savetxt("zzz_lapB_L16_d10_N10",lapB)
np.savetxt("zzz_parA_L16_d10_N10",parP)
np.savetxt("zzz_parB_L16_d10_N10",parM)
np.savetxt("zzz_wlist_d16_N10",wlist)
"""

phALL=np.loadtxt("zzz_phA_L16_d10")
parPLL=np.loadtxt("zzz_parA_L16_d10")

phAL=np.loadtxt("zzz_phA_L16_d10_N10")
phBL=np.loadtxt("zzz_phB_L16_d10_N10")
lapAL=np.loadtxt("zzz_lapA_L16_d10_N10")
lapBL=np.loadtxt("zzz_lapB_L16_d10_N10")
parPL=np.loadtxt("zzz_parA_L16_d10_N10")
parML=np.loadtxt("zzz_parB_L16_d10_N10")
wlistL=np.loadtxt("zzz_wlist_d16_N10")

plt.figure("Phase Error")
plt.scatter(wlistL,phAL,s=50)
plt.scatter(wlistL,phALL,s=20)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()

plt.figure("Parity Error")
plt.scatter(wlistL,parPL,s=50)
plt.scatter(wlistL,parPLL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.show()

plt.figure("Lap Error")
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.show()
