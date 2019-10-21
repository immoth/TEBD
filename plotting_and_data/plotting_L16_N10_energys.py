# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_TparP_L16_d10_N2",abs(np.array(TparP)))
np.savetxt("zzz_TparM_L16_d10_N2",-abs(np.array(TparM)))
np.savetxt("zzz_EmidP_L16_d10_N2",np.real(np.array(EmidP)))
np.savetxt("zzz_EmidM_L16_d10_N2",np.real(np.array(EmidM)))
np.savetxt("zzz_EendP_L16_d10_N2",np.real(np.array(EendP)))
np.savetxt("zzz_EendM_L16_d10_N2",np.real(np.array(EendM)))
np.savetxt("zzz_wlistE_d16_N2",wlist)
"""

TparPL=np.loadtxt("zzz_TparP_L16_d10_N2")
TparML=np.loadtxt("zzz_TparM_L16_d10_N2")
EmidPL=np.loadtxt("zzz_EmidP_L16_d10_N2")
EmidML=np.loadtxt("zzz_EmidM_L16_d10_N2")
EendPL=np.loadtxt("zzz_EendP_L16_d10_N2")
EendML=np.loadtxt("zzz_EendM_L16_d10_N2")
wlistL=np.loadtxt("zzz_wlistE_d16_N2")

plt.figure("Total Parity")
plt.scatter(wlistL,TparPL,s=50)
plt.scatter(wlistL,TparML,s=50)
plt.xlabel("Wiat Time")
plt.ylabel("Total Parity")
plt.savefig("zzy_Tpar_L16_d10_N2.svg")
plt.show()

plt.figure("Total Parity Offset")
plt.scatter(wlistL,1-TparPL,s=50)
plt.scatter(wlistL,1+TparML,s=50)
plt.ylim(-0.00005,0.00005)
plt.xlabel("Wiat Time")
plt.ylabel("Total Parity Offset")
plt.savefig("zzy_TparO_L16_d10_N2.svg")
plt.show()

plt.figure("Energy Difference")
plt.plot(wlistL,EmidPL-EmidML)
plt.plot(wlistL,EendPL-EendML)
plt.xlabel("Wiat Time")
plt.ylabel("Energy Difference")
plt.savefig("zzy_Ediff_L16_d10_N2.svg")
plt.show()

plt.figure("Energy Gap")
plt.plot(wlistL,EmidPL-EmidML)
plt.plot(wlistL,EendPL-EendML)
plt.ylim(-Delta,Delta)
plt.xlabel("Wiat Time")
plt.ylabel("Energy Difference")
plt.savefig("zzy_EdiffGap_L16_d10_N2.svg")
plt.show()


