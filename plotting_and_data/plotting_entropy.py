# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:59:47 2019

@author: jsten
"""
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import pickle
import pickle_save as ps
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')


#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\epl_zapB2_L16_W"+str(wait)+".txt",eplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\eml_zapB2_L16_W"+str(wait)+".txt",emlist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\epl_L16_W"+str(wait)+".txt",eplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\eml_L16_W"+str(wait)+".txt",emlist)

with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\ppl_L16_W950.txt","rb") as f:
    ppL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\pml_L16_W950.txt","rb") as f:
    pmL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\epl_L16_W950.txt","rb") as f:
    epL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\eml_L16_W950.txt","rb") as f:
    emL=pickle.load(f)

plt.figure("Entropy")
plt.imshow(np.transpose(np.array(epL,dtype=float)), aspect="auto", extent=[-100,950,14,0])
plt.xlabel("Time")
plt.ylabel("Bond")
plt.show()

plt.figure("Local Parity")
plt.imshow(np.transpose(np.array(ppL,dtype=float)), aspect="auto", extent=[-100,950,15,0])
plt.xlabel("Time")
plt.ylabel("Site")
plt.show()

phpL=np.loadtxt("zzz_phA_L16_d50")
phmL=np.loadtxt("zzz_phB_L16_d50")
wlistL=np.loadtxt("zzz_wlist_d50")

wlistL=[]
for t in range(0,len(phpL)):
    wlistL.append(t*50)

plt.figure("Phase Error")
plt.scatter(wlistL,phpL,s=100)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.show()

