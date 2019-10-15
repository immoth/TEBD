# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:34:04 2019

@author: jsten
"""
import numpy as np
import pickle
import pickle_save as ps
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('ggplot')


#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\ppl_L16_W"+str(wait)+".txt",pplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\pml_L16_W"+str(wait)+".txt",pmlist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\epl_L16_W"+str(wait)+".txt",eplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\eml_L16_W"+str(wait)+".txt",emlist)


"""
php.append(np.imag(np.log(ME.ME(ymt,gxMPO(gxlist,L),ypt))))
phm.append(np.pi+np.imag(np.log(ME.ME(ymt,gyMPO(gxlist,L),ypt))))
wlist.append(wait)
"""

np.savetxt("zzz_phA_L16_d50",php)
np.savetxt("zzz_phB_L16_d50",phm)
np.savetxt("zzz_wlist_L16_d50",wlist)



phpL=np.loadtxt("zzz_phA_L16_d50")
phmL=np.loadtxt("zzz_phB_L16_d50")
wlistL=np.loadtxt("zzz_wlist_d50")

"""
php2L=np.loadtxt("zzz_phA_L10")
wlist2L=np.loadtxt("zzz_wlist")
"""

plt.scatter(wlist,phpL,s=100)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
#plt.scatter(wlist2L,php2L)
plt.show()


#ws=str(wait)
ws="300"
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\ppl_L16_W"+ws+".txt","rb") as f:
    ppL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\pml_L16_W"+ws+".txt","rb") as f:
    pmL=pickle.load(f)


sites=[]
for l in range(0,L):
    sites.append(l)


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    xs=sites
    yp=ppL[i]
    ym=pmL[i]
    ax1.clear()
    plt.ylim(-0.3,0.3)
    plt.xlabel("Site")
    plt.ylabel("Local Parity")
    ax1.plot(xs, yp, linewidth=10)
    ax1.plot(xs, ym, linewidth=5)
    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()

