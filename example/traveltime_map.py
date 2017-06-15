import numpy as np
import pylab as plt
from traveltime import eikonal


#%% TRAVELTIME MAP
dx=0.1;
x = np.arange(-1,6,dx)
y = np.arange(-1,13,dx)

x_src = np.array([1, 2.50, 2.5, 1])
y_src = np.array([1, 5, 10, 1])
S=np.array([x_src,y_src]).transpose()

xx,yy = np.meshgrid(x,y)
phi = -1*np.ones_like(xx)


V = 0.1*np.ones_like(xx);
#V[yy>6] = 13;
#V[np.logical_and(np.abs(yy)>7, xx>2.5)] = 5

t_map = eikonal(x,y,[],V,S)


plt.subplot(1,2,2)
plt.pcolor(x,y,t_map[0])

plt.subplot(1,2,1)
plt.pcolor(x,y,V)
plt.show

