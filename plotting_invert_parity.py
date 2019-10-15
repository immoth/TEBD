# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:29:43 2019

@author: jsten
"""

import copy
import matplotlib.pyplot

parP_L4=np.loadtxt("zzz_parP_L4")
parP_L6=np.loadtxt("zzz_parP_L6")
parP_L8=np.loadtxt("zzz_parP_L8")
parP_L10=np.loadtxt("zzz_parP_L10")
parP_L12=np.loadtxt("zzz_parP_L12")
parP_L14=np.loadtxt("zzz_parP_L14")
parP_L16=np.loadtxt("zzz_parP_L16")
parP_L18=np.loadtxt("zzz_parP_L18")
parP_L20=np.loadtxt("zzz_parP_L20")

parM_L4=np.loadtxt("zzz_parM_L4")
parM_L6=np.loadtxt("zzz_parM_L6")
parM_L8=np.loadtxt("zzz_parM_L8")
parM_L10=np.loadtxt("zzz_parM_L10")
parM_L12=np.loadtxt("zzz_parM_L12")
parM_L14=np.loadtxt("zzz_parM_L14")
parM_L16=np.loadtxt("zzz_parM_L16")
parM_L18=np.loadtxt("zzz_parM_L18")
parM_L20=np.loadtxt("zzz_parM_L20")

parP_L=[parP_L4,parP_L6,parP_L8,parP_L10,parP_L12,parP_L14,parP_L16,parP_L18,parP_L20]
parM_L=[parM_L4,parM_L6,parM_L8,parM_L10,parM_L12,parM_L14,parM_L16,parM_L18,parM_L20]


parP_t=np.transpose(parP_L)
parM_t=np.transpose(parM_L)

parP_nt=copy.deepcopy(parP_t)
parM_nt=copy.deepcopy(parM_t)
for i in range(0,len(parP_t)):
    for j in range(0,len(parP_t[0])):
        parP_nt[i][j]=1-abs(parP_t[i][j])
        parM_nt[i][j]=1-abs(parM_t[i][j])
        

llist=[4,6,8,10,12,14,16,18,20]

plt.scatter(llist,parP_nt[0],s=200)
#plt.savefig("zzy_parP_t0.svg")
plt.show()
plt.scatter(llist,parP_nt[1],s=200)
#plt.savefig("zzy_parP_t1.svg")
plt.show()
plt.scatter(llist,parP_nt[2],s=200)
#plt.savefig("zzy_parity_t2.svg")
plt.show()
plt.scatter(llist,parP_nt[3],s=200)
#plt.savefig("zzy_parP_t3.svg")
plt.show()
plt.scatter(llist,parP_nt[4],s=200)
#plt.savefig("zzy_parP_t4.svg")
plt.show()
plt.scatter(llist,parP_nt[5],s=200)
#plt.savefig("zzy_parP_t5.svg")
plt.show()
plt.scatter(llist,parP_nt[6],s=200)
#plt.savefig("zzy_parity_t6.svg")
plt.show()
plt.scatter(llist,parP_nt[7],s=200)
#plt.savefig("zzy_parP_t7.svg")
plt.show()
plt.scatter(llist,parP_nt[8],s=200)
#plt.savefig("zzy_parP_t8.svg")
plt.show()
plt.scatter(llist,parP_nt[9],s=200)
#plt.savefig("zzy_parP_t9.svg")
plt.show()

plt.scatter(llist,parM_nt[0],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t0.svg")
plt.show()
plt.scatter(llist,parM_nt[1],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t1.svg")
plt.show()
plt.scatter(llist,parM_nt[2],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t2.svg")
plt.show()
plt.scatter(llist,parM_nt[3],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t3.svg")
plt.show()
plt.scatter(llist,parM_nt[4],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t4.svg")
plt.show()
plt.scatter(llist,parM_nt[5],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t5.svg")
plt.show()
plt.scatter(llist,parM_nt[6],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t6.svg")
plt.show()
plt.scatter(llist,parM_nt[7],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t7.svg")
plt.show()
plt.scatter(llist,parM_nt[8],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t8.svg")
plt.show()
plt.scatter(llist,parM_nt[9],s=200,color='goldenrod')
#plt.savefig("zzy_parM_t9.svg")
plt.show()






















