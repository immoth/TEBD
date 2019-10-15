# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:48:07 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:13:50 2019

@author: jsten
"""

import matplotlib.pyplot as plt

#np.savetxt("zzz_zapEnd_phA_L16_d10",phA)
#np.savetxt("zzz_zapEnd_phB_L16_d10",phB)
#np.savetxt("zzz_zapEnd_lapA_L16_d10",lapA)
#np.savetxt("zzz_zapEnd_lapB_L16_d10",lapB)
#np.savetxt("zzz_zapEnd_parA_L16_d10",parP)
#np.savetxt("zzz_zapEnd_parB_L16_d10",parM)
#np.savetxt("zzz_zapEnd_wlist_d16",wlist)

phAL=np.loadtxt("zzz_zapEnd_phA_L16_d10")
phBL=np.loadtxt("zzz_zapEnd_phB_L16_d10")
lapAL=np.loadtxt("zzz_zapEnd_lapA_L16_d10")
lapBL=np.loadtxt("zzz_zapEnd_lapB_L16_d10")
parPL=np.loadtxt("zzz_zapEnd_parA_L16_d10")
parML=np.loadtxt("zzz_zapEnd_parB_L16_d10")
wlistL=np.loadtxt("zzz_zapEnd_wlist_d16")

plt.figure("Phase Error")
plt.scatter(wlist,phAL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()

plt.figure("Parity Error")
plt.scatter(wlist,parPL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.show()