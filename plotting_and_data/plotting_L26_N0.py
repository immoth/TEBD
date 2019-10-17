# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_phA_L26_d10_N0",phA)
np.savetxt("zzz_phB_L26_d10_N0",phB)
np.savetxt("zzz_lapA_L26_d10_N0",lapA)
np.savetxt("zzz_lapB_L26_d10_N0",lapB)
np.savetxt("zzz_parA_L26_d10_N0",parP)
np.savetxt("zzz_parB_L26_d10_N0",parM)
np.savetxt("zzz_wlist_d26_N0",wlist)
"""

phAm10=np.loadtxt("zzz_phA_L26_d10_Nm10")
phBm10=np.loadtxt("zzz_phB_L26_d10_Nm10")
lapAm10=np.loadtxt("zzz_lapA_L26_d10_Nm10")
lapBm10=np.loadtxt("zzz_lapB_L26_d10_Nm10")
parPm10=np.loadtxt("zzz_parA_L26_d10_Nm10")
parMm10=np.loadtxt("zzz_parB_L26_d10_Nm10")
wlistL=np.loadtxt("zzz_wlist_d26_Nm10")

phAm8=np.loadtxt("zzz_phA_L26_d10_Nm8")
lapAm8=np.loadtxt("zzz_lapA_L26_d10_Nm8")
parPm8=np.loadtxt("zzz_parA_L26_d10_Nm8")
parPm8=np.loadtxt("zzz_parA_L26_d10_Nm8")

phAN2=np.loadtxt("zzz_phA_L26_d10")
lapAN2=np.loadtxt("zzz_lapA_L26_d10")
parPN2=np.loadtxt("zzz_parA_L26_d10")
parPN2=np.loadtxt("zzz_parA_L26_d10")

phAN0=np.loadtxt("zzz_phA_L26_d10_N0")
lapAN0=np.loadtxt("zzz_lapA_L26_d10_N0")
parPN0=np.loadtxt("zzz_parA_L26_d10_N0")
parPN0=np.loadtxt("zzz_parA_L26_d10_N0")
wlistN0=np.loadtxt("zzz_wlist_d26_N0")

"""
phA10=np.loadtxt("zzz_phA_L26_d10_N10")
lapA10=np.loadtxt("zzz_lapA_L26_d10_N10")
parP10=np.loadtxt("zzz_parA_L26_d10_N10")
parP10=np.loadtxt("zzz_parA_L26_d10_N10")
"""

plt.figure("Phase Error")
#plt.scatter(wlistL,phA10,s=50)
plt.scatter(wlistL,phAm8,s=30)
plt.scatter(wlistL,phAm10,s=20)
plt.scatter(wlistL,phAN2,s=10)
plt.scatter(wlistN0,phAN0,s=5)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.savefig("zzy_phA_L26_d10_N.svg")
plt.show()

plt.figure("Parity Error")
#plt.scatter(wlistL,parP10,s=50)
plt.scatter(wlistL,parPm8,s=30)
plt.scatter(wlistL,parPL,s=20)
plt.scatter(wlistL,parPN2,s=10)
plt.scatter(wlistN0,parPN0,s=5)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_parPA_L26_d10_N.svg")
plt.show()

plt.figure("Lap Error")
#plt.scatter(wlistL,lapA10,s=50)
plt.scatter(wlistL,lapAm8,s=30)
plt.scatter(wlistL,lapAL,s=20)
plt.scatter(wlistL,lapAN2,s=10)
plt.scatter(wlistN0,lapAN0,s=5)
plt.xlabel("Wiat Time")
plt.ylabel("Lap Error")
plt.savefig("zzy_lapA_L26_d10_N.svg")
plt.show()
