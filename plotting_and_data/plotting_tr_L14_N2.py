# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_tr_phA_L14_d10_N2",phA)
np.savetxt("zzz_tr_phB_L14_d10_N2",phB)
np.savetxt("zzz_tr_lapA_L14_d10_N2",lapA)
np.savetxt("zzz_tr_lapB_L14_d10_N2",lapB)
np.savetxt("zzz_tr_parA_L14_d10_N2",parP)
np.savetxt("zzz_tr_parB_L14_d10_N2",parM)
np.savetxt("zzz_tr_Ntlist_L14_d10_N2",Ntlist)

np.savetxt("zzz_tr_TparP_L14_d10_N2",np.real(TparP))
np.savetxt("zzz_tr_TparM_L14_d10_N2",np.real(TparM))
np.savetxt("zzz_tr_EendP_L14_d10_N2",np.real(EendP))
np.savetxt("zzz_tr_EendM_L14_d10_N2",np.real(EendM))
np.savetxt("zzz_tr_EmidP_L14_d10_N2",np.real(EmidP))
np.savetxt("zzz_tr_EmidM_L14_d10_N2",np.real(EmidM))

np.savetxt("zzz_tr_timeL_L14_d10_N2",np.real(timeL))
"""


phAL=np.loadtxt("zzz_tr_phA_L14_d10_N2")
phBL=np.loadtxt("zzz_tr_phB_L14_d10_N2")
lapAL=np.loadtxt("zzz_tr_lapA_L14_d10_N2")
lapBL=np.loadtxt("zzz_tr_lapB_L14_d10_N2")
parPL=np.loadtxt("zzz_tr_parA_L14_d10_N2")
parML=np.loadtxt("zzz_tr_parB_L14_d10_N2")
wlistL=np.loadtxt("zzz_tr_Ntlist_L14_d10_N2")

TparPL=np.loadtxt("zzz_tr_TparP_L14_d10_N2")
TparML=np.loadtxt("zzz_tr_TparM_L14_d10_N2")
EendPL=np.loadtxt("zzz_tr_EendP_L14_d10_N2")
EendML=np.loadtxt("zzz_tr_EendM_L14_d10_N2")

timeLL=np.loadtxt("zzz_tr_timeL_L14_d10_N2")


plt.figure("Phase Error")
#plt.xlim(-0.01,0.1)
#plt.ylim(-0.01,0.02)
plt.scatter(wlistL,phAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Phase Error")
plt.savefig("zzy_tr_phA_L14_d10_N2.svg")
plt.show()

plt.figure("Parity Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.1)
plt.scatter(wlistL,parPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_tr_parA_L14_d10_N2.svg")
plt.show()

plt.figure("Lap Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Lap Error")
plt.savefig("zzy_tr_lapA_L14_d10_N2.svg")
plt.show()


plt.figure("Total Parity")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,TparPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Total Parity")
plt.savefig("zzy_tr_TparP_L14_d10_N2.svg")
plt.show()

plt.figure("Energy")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,EendPL-EendML,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Energy")
plt.savefig("zzy_tr_EendPL_L14_d10_N2.svg")
plt.show()

