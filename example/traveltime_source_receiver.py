import sys

import numpy as np
import pylab as plt
import traveltime as tt

#%% CREATE REFERENCE VELOCITY MODEL
dx=0.1;
x = np.arange(-1,6,dx)
y = np.arange(-1,13,dx)
xx,yy = np.meshgrid(x,y)
V = 0.1*np.ones_like(xx);
V[yy>6] = 0.15;
V[np.logical_and(np.abs(yy)>7, xx>2.5)] = 0.18;


#%% SET SOURCE AND RECEIVERS
nr=14;
ns=1;
x_rec=5*np.ones([nr])
y_rec = np.linspace(1, 12,nr);
R=np.array([x_rec,y_rec]).transpose()
S=np.zeros_like(R)
S[:,0]=0;
S[:,1]=5;

#%% PLOT MODEL
plt.pcolor(x,y,V)
plt.axes().set_aspect('equal')

for i in range(nr):
    #plt.plot(R[:,0],R[:,1],'v*')
    plt.plot([S[i,0],R[i,0]],[S[i,1],R[i,1]],'w-')
plt.axes().set_aspect('equal')
plt.gca().invert_yaxis()
plt.xlabel('X (m)')
plt.ylabel('Z (m)')
plt.colorbar()
plt.show()


#%% FULL EIKONAL SOLUTION
#t_map =tt.eikonal(x,y,[],V,S)
#plt.pcolor(x,y,t_map[0])

#%%

t = tt.eikonal_traveltime(x,y,[],V,S,R)
plt.plot(t,R[:,1],'-*')
plt.gca().invert_yaxis()
plt.xlabel('Traveltime (ns)')
plt.ylabel('Z (m)')
plt.show()
