# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:46:03 2019

@author: jsten
"""
import numpy as np
import matplotlib.pyplot as plt

wlist=np.loadtxt("zzz_wlist")

phA_L4=np.loadtxt("zzz_phA_L4")
phA_L6=np.loadtxt("zzz_phA_L6")
phA_L8=np.loadtxt("zzz_phA_L8")
phA_L10=np.loadtxt("zzz_phA_L10")
phA_L12=np.loadtxt("zzz_phA_L12")
phA_L14=np.loadtxt("zzz_phA_L14")
phA_L16=np.loadtxt("zzz_phA_L16")
phA_L18=np.loadtxt("zzz_phA_L18")
phA_L20=np.loadtxt("zzz_phA_L20")

phA_L=np.array([phA_L4,phA_L6,phA_L8,phA_L10,phA_L12,phA_L14,phA_L16,phA_L18,phA_L20])
phA_t=np.transpose(phA_L)

llist=[4,6,8,10,12,14,16,18,20]

plt.scatter(llist,np.log(phA_t[0]),s=200)
#plt.savefig("zzy_t0_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[1]),s=200)
#plt.savefig("zzy_t1_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[2]),s=200)
#plt.savefig("zzy_t2_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[3]),s=200)
#plt.savefig("zzy_t3_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[4]),s=200)
#plt.savefig("zzy_t4_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[5]),s=200)
#plt.savefig("zzy_t5_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[6]),s=200)
#plt.savefig("zzy_t6_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[7]),s=200)
#plt.savefig("zzy_t7_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[8]),s=200)
#plt.savefig("zzy_t8_phase_log.svg")
plt.show()
plt.scatter(llist,np.log(phA_t[9]),s=200)
#plt.savefig("zzy_t9_phase_log.svg")
plt.show()




