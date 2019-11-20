# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:50:42 2019

@author: jsten
"""

muL=0.2
tuaL=1
DeltaL=0.7
VmaxL=0.1
NtL=500
dtL=0.01
BDL=40
alphaL=0

L10=10
L12=12
L14=14
L16=16
L18=18
L20=20
L22=22


directory="C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_clean\\data_std\\"
directoryF="C:\\Users\\jsten\\Documents\\Reaserch\\Interaction Error\\TEBD_clean\\figures_std\\"

fileL10="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L10)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL12="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L12)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL14="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L14)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL16="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L16)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL18="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L18)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL20="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L20)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
fileL22="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str(L22)+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)

with open(directory+fileL10+"_wlist"+".txt","rb") as f:
    wlistL=pickle.load(f)
with open(directory+fileL12+"_phA"+".txt","rb") as f:
    phAL12=pickle.load(f)
with open(directory+fileL14+"_phA"+".txt","rb") as f:
    phAL14=pickle.load(f)
with open(directory+fileL16+"_phA"+".txt","rb") as f:
    phAL16=pickle.load(f)
with open(directory+fileL18+"_phA"+".txt","rb") as f:
    phAL18=pickle.load(f)
with open(directory+fileL20+"_phA"+".txt","rb") as f:
    phAL20=pickle.load(f)
with open(directory+fileL22+"_phA"+".txt","rb") as f:
    phAL22=pickle.load(f)
    
file="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str("L10_12_14_16_18_20_22")+"_tr"+str(NtL)+"_tw"+str('F')+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)    
plt.figure("Phase Error")
#plt.xlim(-0.01,0.1)
#plt.ylim(-0.00,0.002)
plt.scatter(wlistL,phAL10,s=50)
plt.scatter(wlistL,phAL12,s=50)
plt.scatter(wlistL,phAL14,s=50)
plt.scatter(wlistL,phAL16,s=50)
plt.scatter(wlistL,phAL18,s=50)
plt.scatter(wlistL,phAL20,s=50)
plt.scatter(wlistL,phAL22,s=40)
plt.xlabel("Ramp Time")
plt.ylabel("Phase Error")
plt.savefig(directoryF+file+"_phA"+".svg")
plt.show()

phAl=[phAL10,phAL12,phAL14,phAL16,phAL18,phAL20,phAL22]

phAvL=[]
Llist=[]
for i in range(0,7):
    phAvL.append(phAl[i][99])
    Llist.append(10+2*i)
    

file="_m"+str(muL)+"_J"+str(tuaL)+"_D"+str(DeltaL)+"_V"+str(VmaxL)+"_L"+str('F')+"_tr"+str(NtL)+"_tw"+str(3000)+"_dt"+str(dtL)+"_BD"+str(BD)+"_N"+str(n2-n1)+"_alpha"+str(alphaL)
plt.figure("Phase Error vs L")
#plt.xlim(-0.01,0.1)
#plt.ylim(-0.00,0.002)
plt.yscale("log")
plt.scatter(Llist,phAvL,s=50)
plt.xlabel("Ramp Time")
plt.ylabel("Phase Error")
plt.savefig(directoryF+file+"_phA"+".svg")
plt.show()



