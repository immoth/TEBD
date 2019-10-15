# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:17:11 2019

@author: jsten
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pickle



with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\ppl_L10_W"+str(wait)+".txt","rb") as f:
    ppL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\pml_L10_W"+str(wait)+".txt","rb") as f:
    pmL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\epl_L10_W"+str(wait)+".txt","rb") as f:
    epL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_BondControl\pdata\eml_L10_W"+str(wait)+".txt","rb") as f:
    emL=pickle.load(f)

"""
ppL=pplist
pmL=pmlist
epL=eplist
emL=emlist
"""

style.use('fivethirtyeight')


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
    ax1.plot(xs, yp)
    ax1.plot(xs, ym)
    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()


"""
def animate(i):
    xs=sites
    yp=eplist[i]
    ym=emlist[i]
    ax1.clear()
    plt.ylim(-1.1,1.1)
    ax1.plot(xs, yp)
    ax1.plot(xs, ym)
    
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
"""

"tools->prefences->ipython consal->graphics->backend=automatic"
"%matplotlib qt5"



