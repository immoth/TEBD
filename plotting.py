# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:18:28 2019

@author: jsten
"""

import numpy as np
import matplotlib.pyplot as plt

"""
np.savetxt("zzz_wlist_L4",wlist)
np.savetxt("zzz_flE_L4",flE)
np.savetxt("zzz_phE_L4",phE)
np.savetxt("zzz_flED_L4",flED)
np.savetxt("zzz_phED_L4",phED)
"""
"""
np.savetxt("zzz_pwlist_L4",wlist)
np.savetxt("zzz_ppE_L4",ppE)
np.savetxt("zzz_ppED_L4",ppED)
np.savetxt("zzz_pmE_L4",pmE)
np.savetxt("zzz_pmED_L4",pmED)
"""


wlistL4=np.loadtxt("zzz_wlist_L4")
flEL4=np.loadtxt("zzz_flE_L4")
phEL4=np.loadtxt("zzz_phE_L4")
flEDL4=np.loadtxt("zzz_flED_L4")
phEDL4=np.loadtxt("zzz_phED_L4")

plt.scatter(wlistL4,flEL4,s=200)
plt.scatter(wlistL4,flEDL4,s=50)
plt.scatter(wlistL4,phEL4,s=200)
plt.scatter(wlistL4,phEDL4,s=50)
#plt.savefig("yyy_L4.svg")
plt.show()

wlistL5=np.loadtxt("zzz_wlist_L5")
flEL5=np.loadtxt("zzz_flE_L5")
phEL5=np.loadtxt("zzz_phE_L5")
flEDL5=np.loadtxt("zzz_flED_L5")
phEDL5=np.loadtxt("zzz_phED_L5")

plt.scatter(wlistL5,flEL5,s=200)
plt.scatter(wlistL5,flEDL5,s=50)
plt.scatter(wlistL5,phEL5,s=200)
plt.scatter(wlistL5,phEDL5,s=50)
#plt.savefig("yyy_L5.svg")
plt.show()


wlistL6=np.loadtxt("zzz_wlist_L6")
flEL6=np.loadtxt("zzz_flE_L6")
phEL6=np.loadtxt("zzz_phE_L6")
flEDL6=np.loadtxt("zzz_flED_L6")
phEDL6=np.loadtxt("zzz_phED_L6")

plt.scatter(wlistL6,flEL6,s=200)
plt.scatter(wlistL6,flEDL6,s=50)
plt.scatter(wlistL6,phEL6,s=200)
plt.scatter(wlistL6,phEDL6,s=50)
#plt.savefig("yyy_L6.svg")
plt.show()


wlistL7=np.loadtxt("zzz_wlist_L7")
flEL7=np.loadtxt("zzz_flE_L7")
phEL7=np.loadtxt("zzz_phE_L7")
flEDL7=np.loadtxt("zzz_flED_L7")
phEDL7=np.loadtxt("zzz_phED_L7")

plt.scatter(wlistL7,flEL7,s=200)
plt.scatter(wlistL7,flEDL7,s=50)
plt.scatter(wlistL7,phEL7,s=200)
plt.scatter(wlistL7,phEDL7,s=50)
#plt.savefig("yyy_L7.svg")
plt.show()


wlistL8=np.loadtxt("zzz_wlist_L8")
flEL8=np.loadtxt("zzz_flE_L8")
phEL8=np.loadtxt("zzz_phE_L8")
flEDL8=np.loadtxt("zzz_flED_L8")
phEDL8=np.loadtxt("zzz_phED_L8")

plt.scatter(wlistL8,flEL8,s=200)
plt.scatter(wlistL8,flEDL8,s=50)
plt.scatter(wlistL8,phEL8,s=200)
plt.scatter(wlistL8,phEDL8,s=50)
#plt.savefig("yyy_L8.svg")
plt.show()



pwlistL4=np.loadtxt("zzz_pwlist_L4")
ppEL4=np.loadtxt("zzz_ppE_L4")
ppEDL4=np.loadtxt("zzz_ppED_L4")
pmEL4=np.loadtxt("zzz_pmE_L4")
pmEDL4=np.loadtxt("zzz_pmED_L4")

plt.scatter(pwlistL4,ppEL4,s=200)
plt.scatter(pwlistL4,ppEDL4,s=50)
plt.scatter(pwlistL4,pmEL4,s=200)
plt.scatter(pwlistL4,pmEDL4,s=50)
#plt.savefig("yyy_pL4.svg")
plt.show()



pwlistL6=np.loadtxt("zzz_pwlist_L6")
ppEL6=np.loadtxt("zzz_ppE_L6")
ppEDL6=np.loadtxt("zzz_ppED_L6")
pmEL6=np.loadtxt("zzz_pmE_L6")
pmEDL6=np.loadtxt("zzz_pmED_L6")

plt.scatter(pwlistL6,ppEL6,s=200)
plt.scatter(pwlistL6,ppEDL6,s=50)
plt.scatter(pwlistL6,pmEL6,s=200)
plt.scatter(pwlistL6,pmEDL6,s=50)
#plt.savefig("yyy_pL6.svg")
plt.show()















