# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_phA_L26_d10_Nm8",phA)
np.savetxt("zzz_phB_L26_d10_Nm8",phB)
np.savetxt("zzz_lapA_L26_d10_Nm8",lapA)
np.savetxt("zzz_lapB_L26_d10_Nm8",lapB)
np.savetxt("zzz_parA_L26_d10_Nm8",parP)
np.savetxt("zzz_parB_L26_d10_Nm8",parM)
np.savetxt("zzz_wlist_d26_Nm8",wlist)
"""

phAL=np.loadtxt("zzz_phA_L26_d10_Nm8")
phBL=np.loadtxt("zzz_phB_L26_d10_Nm8")
lapAL=np.loadtxt("zzz_lapA_L26_d10_Nm8")
lapBL=np.loadtxt("zzz_lapB_L26_d10_Nm8")
parPL=np.loadtxt("zzz_parA_L26_d10_Nm8")
parML=np.loadtxt("zzz_parB_L26_d10_Nm8")
wlistL=np.loadtxt("zzz_wlist_d26_Nm8")

phALL=np.loadtxt("zzz_phA_L26_d10")
lapALL=np.loadtxt("zzz_lapA_L26_d10")
parPLL=np.loadtxt("zzz_parA_L26_d10")
parPLLL=np.loadtxt("zzz_parA_L16_d10")

phALLL=np.loadtxt("zzz_phA_L26_d10_N10")
lapALLL=np.loadtxt("zzz_lapA_L26_d10_N10")
parPLLL=np.loadtxt("zzz_parA_L26_d10_N10")
parPLLLL=np.loadtxt("zzz_parA_L16_d10_N10")


plt.figure("Phase Error")
plt.scatter(wlistL,phAL,s=50)
plt.scatter(wlistL,phALL,s=30)
plt.scatter(wlistL,phALLL,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()

plt.figure("Parity Error")
plt.scatter(wlistL,parPL,s=50)
plt.scatter(wlistL,parPLL,s=30)
plt.scatter(wlistL,parPLLL,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.show()

plt.figure("Lap Error")
plt.scatter(wlistL,lapAL,s=50)
plt.scatter(wlistL,lapALL,s=30)
plt.scatter(wlistL,lapALLL,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Lap Error")
plt.show()
