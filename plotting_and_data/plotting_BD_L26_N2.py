# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np

fileparm="_BD_L26_d2_N2+"


np.savetxt("zzz"+fileparm+"phA",phA)
np.savetxt("zzz"+fileparm+"phB",phB)
np.savetxt("zzz"+fileparm+"lapA",lapA)
np.savetxt("zzz"+fileparm+"lapB",lapB)
np.savetxt("zzz"+fileparm+"parA",parP)
np.savetxt("zzz"+fileparm+"parB",parM)
np.savetxt("zzz"+fileparm+"Ntlist",BDlist)

np.savetxt("zzz"+fileparm+"TparP",np.real(TparP))
np.savetxt("zzz"+fileparm+"TparM",np.real(TparM))
np.savetxt("zzz"+fileparm+"EendP",np.real(EendP))
np.savetxt("zzz"+fileparm+"EendM",np.real(EendM))
np.savetxt("zzz"+fileparm+"EmidP",np.real(EmidP))
np.savetxt("zzz"+fileparm+"EmidM",np.real(EmidM))

np.savetxt("zzz"+fileparm+"timeL",np.real(timeL))



phAL=np.loadtxt("zzz"+fileparm+"phA")
phBL=np.loadtxt("zzz"+fileparm+"phB")
lapAL=np.loadtxt("zzz"+fileparm+"lapA")
lapBL=np.loadtxt("zzz"+fileparm+"lapB")
parPL=np.loadtxt("zzz"+fileparm+"parA")
parML=np.loadtxt("zzz"+fileparm+"parB")
wlistL=np.loadtxt("zzz"+fileparm+"Ntlist")

TparPL=np.loadtxt("zzz"+fileparm+"TparP")
TparML=np.loadtxt("zzz"+fileparm+"TparM")
EendPL=np.loadtxt("zzz"+fileparm+"EendP")
EendML=np.loadtxt("zzz"+fileparm+"EendM")

timeLL=np.loadtxt("zzz"+fileparm+"timeL")


plt.figure("Phase Error")
#plt.xlim(-0.01,0.1)
#plt.ylim(-0.01,0.02)
plt.scatter(wlistL,phAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Phase Error")
plt.savefig("zzy"+fileparm+"phA.svg")
plt.show()

plt.figure("Parity Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.1)
plt.scatter(wlistL,parPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Parity Error")
plt.savefig("zzy"+fileparm+"parA.svg")
plt.show()

plt.figure("Lap Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Lap Error")
plt.savefig("zzy"+fileparm+"lapA.svg")
plt.show()


plt.figure("Total Parity")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,TparPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Total Parity")
plt.savefig("zzy"+fileparm+"TparP.svg")
plt.show()

plt.figure("Energy")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,EendPL-EendML,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Energy")
plt.savefig("zzy"+fileparm+"EendPL.svg")
plt.show()

