# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_v_phA_L26_d001_N2",phA)
np.savetxt("zzz_v_phB_L26_d001_N2",phB)
np.savetxt("zzz_v_lapA_L26_d001_N2",lapA)
np.savetxt("zzz_v_lapB_L26_d001_N2",lapB)
np.savetxt("zzz_v_parA_L26_d001_N2",parP)
np.savetxt("zzz_v_parB_L26_d001_N2",parM)
np.savetxt("zzz_v_vlist_L26_d001_N2",vlist)
"""

phAL14=np.loadtxt("zzz_v_phA_L14_d001_N2")

phAL=np.loadtxt("zzz_v_phA_L26_d001_N2")
phBL=np.loadtxt("zzz_v_phB_L26_d001_N2")
lapAL=np.loadtxt("zzz_v_lapA_L26_d001_N2")
lapBL=np.loadtxt("zzz_v_lapB_L26_d001_N2")
parPL=np.loadtxt("zzz_v_parA_L26_d001_N2")
parML=np.loadtxt("zzz_v_parB_L26_d001_N2")
wlistL=np.loadtxt("zzz_v_vlist_L26_d001_N2")

sq=[]
for i in range(0,100):
    sq.append(i*i*0.000001+phAL[0]+i*0.000005)

plt.figure("Phase Error")
plt.xlim(-0.0,0.03)
plt.ylim(-0.00,0.001)
plt.scatter(wlistL,phAL,s=50)
plt.scatter(wlistL,phAL14,s=50)
#plt.scatter(wlistL,sq,s=10)
plt.savefig("zzy_v_phA_L26_d001_N2.svg")
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()


plt.figure("Parity Error")
#plt.xlim(-0.01,0.2)
plt.ylim(-0.0,0.02)
plt.scatter(wlistL,parPL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_v_parA_L26_d001_N2.svg")
plt.show()

plt.figure("Lap Error")
#plt.xlim(-0.01,0.2)
plt.ylim(-0.0,0.015)
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_v_lapA_L26_d001_N2.svg")
plt.show()
