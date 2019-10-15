# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:18:28 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt

"""
np.savetxt("zzz_phA_L20",phA)
np.savetxt("zzz_phB_L20",phB)
np.savetxt("zzz_lapA_L20",lapA)
np.savetxt("zzz_lapB_L20",lapB)
np.savetxt("zzz_parP_L20",np.real(parP))
np.savetxt("zzz_parM_L20",np.real(parM))
np.savetxt("zzz_wlist",wlist)
"""

"""
phA_L=np.loadtxt("zzz_phA_L4")
phB_L=np.loadtxt("zzz_phB_L4")
lapA_L=np.loadtxt("zzz_lapA_L4")
lapB_L=np.loadtxt("zzz_lapB_L4")
parP_L=np.loadtxt("zzz_parP_L4")
parM_L=np.loadtxt("zzz_parM_L4")
wlist=np.loadtxt("zzz_wlist")
"""


phA_L=phA
phB_L=phB
lapA_L=lapA
lapB_L=lapB
parP_L=parP
parM_L=parM
wlist=np.loadtxt("zzz_wlist")


plt.scatter(wlist,phA_L,s=200)
plt.scatter(wlist,phB_L,s=50)
plt.scatter(wlist,lapA_L,s=200)
plt.scatter(wlist,lapB_L,s=50)
#plt.savefig("zzy_L20_phase.svg")
plt.show()

plt.scatter(wlist,parP_L,s=200)
plt.scatter(wlist,parM_L,s=200)
#plt.savefig("zzy_L20_parity.svg")
plt.show()

parP_n=[]
parM_n=[]
for i in range(0,len(parP_L)):
    parP_n.append(1-abs(parP_L[i]))
    parM_n.append(1-abs(parM_L[i]))

plt.scatter(wlist,parP_n,s=200)
plt.scatter(wlist,parM_n,s=200)
plt.savefig("zzy_L4_parity_N.svg")
plt.show()









