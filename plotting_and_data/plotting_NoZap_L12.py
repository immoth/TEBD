# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt

"""
np.savetxt("zzz_NoZap_phA_L12_d10",phA)
np.savetxt("zzz_NoZap_phB_L12_d10",phB)
np.savetxt("zzz_NoZap_lapA_L12_d10",lapA)
np.savetxt("zzz_NoZap_lapB_L12_d10",lapB)
np.savetxt("zzz_NoZap_parA_L12_d10",parP)
np.savetxt("zzz_NoZap_parB_L12_d10",parM)
np.savetxt("zzz_NoZap_wlist_d12",wlist)
"""

phAL=np.loadtxt("zzz_NoZap_phA_L12_d10")
phBL=np.loadtxt("zzz_NoZap_phB_L12_d10")
lapAL=np.loadtxt("zzz_NoZap_lapA_L12_d10")
lapBL=np.loadtxt("zzz_NoZap_lapB_L12_d10")
parPL=np.loadtxt("zzz_NoZap_parA_L12_d10")
parML=np.loadtxt("zzz_NoZap_parB_L12_d10")
wlistL=np.loadtxt("zzz_NoZap_wlist_d12")

phALL=np.loadtxt("zzz_phA_L12_d10")
parPLL=np.loadtxt("zzz_parA_L12_d10")
lapALL=np.loadtxt("zzz_lapA_L12_d10")

plt.figure("Phase Error")
plt.scatter(wlistL,phAL,s=50)
plt.scatter(wlistL,phALL,s=20)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
#plt.savefig("zzy_NoZap_phA_L12_d10.svg")
plt.show()

plt.figure("Parity Error")
plt.scatter(wlistL,parPL,s=50)
plt.scatter(wlistL,parPLL,s=20)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
#plt.savefig("zzy_NoZap_parA_L12_d10.svg")
plt.show()

plt.figure("Overlap Error")
plt.scatter(wlistL,lapAL,s=50)
plt.scatter(wlistL,lapALL,s=20)
plt.xlabel("Wiat Time")
plt.ylabel("Overlap Error")
#plt.savefig("zzy_NoZap_lapA_L12_d10.svg")
plt.show()
