# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:28 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import numpy as np
import pickle

muL=mu
tuaL=tua
DeltaL=Delta
VmaxL=Vmax
LL=L
NtL=Nt
dtL=dt
BDL=BD

directory="C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_clean\\data_std\\"
directoryF="C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_clean\\figures_std\\"

file="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(LL)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BDL)

with open(directory+file+"phA"+".txt","rb") as f:
    phAL=pickle.load(f)
with open(directory+file+"phB"+".txt","rb") as f:
    phBL=pickle.load(f)
with open(directory+file+"lapA"+".txt","rb") as f:
    lapAL=pickle.load(f)
with open(directory+file+"lapB"+".txt","rb") as f:
    lapBL=pickle.load(f)
with open(directory+file+"parP"+".txt","rb") as f:
    parPL=pickle.load(f)
with open(directory+file+"parM"+".txt","rb") as f:
    parML=pickle.load(f)
with open(directory+file+"wlist"+".txt","rb") as f:
    wlistL=pickle.load(f)
with open(directory+file+"TparP"+".txt","rb") as f:
    TparPL=pickle.load(f)
with open(directory+file+"TparM"+".txt","rb") as f:
    TparML=pickle.load(f)
with open(directory+file+"EendP"+".txt","rb") as f:
    EendPL=pickle.load(f)
with open(directory+file+"EendM"+".txt","rb") as f:
    EendML=pickle.load(f)
with open(directory+file+"EmidP"+".txt","rb") as f:
    EmidPL=pickle.load(f)
with open(directory+file+"EmidM"+".txt","rb") as f:
    EmidML=pickle.load(f)



plt.figure("Phase Error")
#plt.xlim(-0.01,0.1)
#plt.ylim(-0.01,0.02)
plt.scatter(wlistL,phAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Phase Error")
plt.savefig(directoryF+file+"_phA"+".svg")
plt.show()

plt.figure("Parity Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.1)
plt.scatter(wlistL,parPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Parity Error")
plt.savefig(directoryF+file+"_parP"+".svg")
plt.show()

plt.figure("Lap Error")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,lapAL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Lap Error")
plt.savefig(directoryF+file+"_lapA"+".svg")
plt.show()


plt.figure("Total Parity")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,TparPL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Total Parity")
plt.savefig(directoryF+file+"_TparP"+".svg")
plt.show()

plt.figure("Energy")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,np.array(EendPL)-np.array(EendML),s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Energy")
plt.savefig(directoryF+file+"_Eend"+".svg")
plt.show()

plt.figure("Mid Energy")
#plt.xlim(-0.01,0.2)
#plt.ylim(-0.01,0.05)
plt.scatter(wlistL,np.array(EmidPL)-np.array(EmidML),s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Energy")
plt.savefig(directoryF+file+"_Emid"+".svg")
plt.show()
