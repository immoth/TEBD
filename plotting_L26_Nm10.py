# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_phA_L26_d10_Nm10",phA)
np.savetxt("zzz_phB_L26_d10_Nm10",phB)
np.savetxt("zzz_lapA_L26_d10_Nm10",lapA)
np.savetxt("zzz_lapB_L26_d10_Nm10",lapB)
np.savetxt("zzz_parA_L26_d10_Nm10",parP)
np.savetxt("zzz_parB_L26_d10_Nm10",parM)
np.savetxt("zzz_wlist_d26_Nm10",wlist)
"""

phAL=np.loadtxt("zzz_phA_L26_d10_Nm10")
phBL=np.loadtxt("zzz_phB_L26_d10_Nm10")
lapAL=np.loadtxt("zzz_lapA_L26_d10_Nm10")
lapBL=np.loadtxt("zzz_lapB_L26_d10_Nm10")
parPL=np.loadtxt("zzz_parA_L26_d10_Nm10")
parML=np.loadtxt("zzz_parB_L26_d10_Nm10")
wlistL=np.loadtxt("zzz_wlist_d26_Nm10")

phAm8=np.loadtxt("zzz_phA_L26_d10_Nm8")
lapAm8=np.loadtxt("zzz_lapA_L26_d10_Nm8")
parPm8=np.loadtxt("zzz_parA_L26_d10_Nm8")
parPm8=np.loadtxt("zzz_parA_L26_d10_Nm8")

phA0=np.loadtxt("zzz_phA_L26_d10")
lapA0=np.loadtxt("zzz_lapA_L26_d10")
parP0=np.loadtxt("zzz_parA_L26_d10")
parP0=np.loadtxt("zzz_parA_L26_d10")

phA10=np.loadtxt("zzz_phA_L26_d10_N10")
lapA10=np.loadtxt("zzz_lapA_L26_d10_N10")
parP10=np.loadtxt("zzz_parA_L26_d10_N10")
parP10=np.loadtxt("zzz_parA_L26_d10_N10")


plt.figure("Phase Error")
#plt.scatter(wlistL,phA10,s=50)
plt.scatter(wlistL,phAm8,s=30)
plt.scatter(wlistL,phAL,s=20)
plt.scatter(wlistL,phA0,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.savefig("zzy_phA_L26_d10_N.svg")
plt.show()

plt.figure("Parity Error")
#plt.scatter(wlistL,parP10,s=50)
plt.scatter(wlistL,parPm8,s=30)
plt.scatter(wlistL,parPL,s=20)
plt.scatter(wlistL,parP0,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_parPA_L26_d10_N.svg")
plt.show()

plt.figure("Lap Error")
#plt.scatter(wlistL,lapA10,s=50)
plt.scatter(wlistL,lapAm8,s=30)
plt.scatter(wlistL,lapAL,s=20)
plt.scatter(wlistL,lapA0,s=10)
plt.xlabel("Wiat Time")
plt.ylabel("Lap Error")
plt.savefig("zzy_lapA_L26_d10_N.svg")
plt.show()
