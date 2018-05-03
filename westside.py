import numpy as np
import matplotlib.pyplot as plt

def modelo(x, lam):
    return np.exp(-x/lam)/lam

def p_lam(lam):
    if lam>=1 and lam<=99:
        return 1/99.0
    else:
        return 0

def p_x_l(obs, lam):
    mul = 1.0
    norm = -np.exp(-20/float(lam))+np.exp(-1/float(lam))
    for dato in obs:
        mul *= modelo(dato,lam)/norm
    return mul

x = [1.2, 2.5, 2.8, 5.0]

p_lam_x = []
for i in range(1,100):
    p_lam_x.append(p_x_l(x, i)*p_lam(i))

plt.figure()
plt.plot(range(1,100),np.asarray(p_lam_x))
plt.savefig("figurita.pdf")


    
