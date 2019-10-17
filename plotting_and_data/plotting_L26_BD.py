# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

"""
np.savetxt("zzz_BD_L26_W3000_ph",phBD)
np.savetxt("zzz_BD_L26_W3000_lap",lapBD)
np.savetxt("zzz_BD_L26_W3000_parBD",parBD)
np.savetxt("zzz_BD_L26_W3000_time1",time1)
np.savetxt("zzz_BD_L26_W3000_time2",time2)
np.savetxt("zzz_BD_L26_W3000_cutl",cutl)
"""

phBDL=np.loadtxt("zzz_BD_L26_W3000_ph")
lapBDL=np.loadtxt("zzz_BD_L26_W3000_lap")
parBDL=np.loadtxt("zzz_BD_L26_W3000_parBD")
time1L=np.loadtxt("zzz_BD_L26_W3000_time1")
time2L=np.loadtxt("zzz_BD_L26_W3000_time2")
BDlL=np.loadtxt("zzz_BD_L26_W3000_cutl")

plt.figure("Phase Error")
plt.scatter(BDlL,phBDL,s=50)
plt.xlabel("Bond Dimension")
plt.ylabel("Phase Error")
plt.show()

plt.figure("Parity Error")
plt.scatter(BDlL,parBDL,s=50)
plt.xlabel("Bond Dimension")
plt.ylabel("Parity Error")
plt.show()

plt.figure("Lap Error")
plt.scatter(BDlL,lapBDL,s=50)
plt.xlabel("Bond Dimension")
plt.ylabel("Lap Error")
plt.show()

plt.figure("Pre Error Run Time")
plt.scatter(BDlL,time1L,s=50)
plt.xlabel("Bond Dimension")
plt.ylabel("Run Time (min)")
plt.show()

plt.figure("Run Time")
plt.scatter(BDlL,time2L,s=50)
plt.xlabel("Bond Dimension")
plt.ylabel("Run Time (min)")
plt.show()

