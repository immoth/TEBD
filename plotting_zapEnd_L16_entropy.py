# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:50:15 2019

@author: jsten
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:17:33 2019

@author: jsten
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:10:48 2019

@author: jsten
"""

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


#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\epl_L16_W"+str(wait)+"_zapEnd.txt",eplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\eml_L16_W"+str(wait)+"_zapEnd.txt",emlist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\ppl_L16_W"+str(wait)+"_zapEnd.txt",pplist)
#ps.save(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\pml_L16_W"+str(wait)+"_zapEnd.txt",pmlist)

with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\ppl_L16_W3000_zapEnd.txt","rb") as f:
    ppL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\pml_L16_W3000_zapEnd.txt","rb") as f:
    pmL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\epl_L16_W3000_zapEnd.txt","rb") as f:
    epL=pickle.load(f)
with open(r"C:\Users\jsten\Documents\Reaserch\Interaction Error\TEBD_functions_EndFix\pdata\eml_L16_W3000_zapEnd.txt","rb") as f:
    emL=pickle.load(f)
    

plt.figure("Entropy")
plt.imshow(np.transpose(np.array(epL,dtype=float)), aspect="auto", extent=[-100,3000,14,0])
plt.xlabel("Time")
plt.ylabel("Bond")
plt.savefig("zzy_zapEnd_epl_L16_W3000.svg")
plt.show()

plt.figure("Local Parity")
plt.imshow(np.transpose(np.array(ppL,dtype=float)), aspect="auto", extent=[-100,3000,15,0])
plt.xlabel("Time")
plt.ylabel("Site")
plt.savefig("zzy_zapEnd_parB_L16_d10.svg")
plt.show()


phpL=np.loadtxt("zzz_zapEnd_phA_L16_d10")
phmL=np.loadtxt("zzz_zapEnd_phB_L16_d10")

wlistL=[]
for t in range(0,len(phpL)):
    wlistL.append(t*10)

plt.figure("Phase Error")
plt.scatter(wlistL,phpL,s=100)
plt.xlabel("Wiat Time")
plt.ylabel("Phase Error")
plt.savefig("zzy_zapEnd_phA_L16_d10.svg")
plt.show()


parAL=np.loadtxt("zzz_zapEnd_parA_L16_d10")
parBL=np.loadtxt("zzz_zapEnd_parB_L16_d10")

plt.figure("Parity Error")
plt.scatter(wlistL,parBL,s=100)
plt.xlabel("Wiat Time")
plt.ylabel("Parity Error")
plt.savefig("zzy_zapEnd_parB_L16_d10")
plt.show()






















