import numpy as np
import pylab as plt
import traveltime as tt

plt.ion(), 

#%% CREATE REFERENCE VELOCITY MODEL
dx=0.1;
x = np.arange(-1,6,dx)
y = np.arange(-1,13,dx)
xx,yy = np.meshgrid(x,y)
V = 0.1*np.ones_like(xx);
V[yy>6] = 0.15;
V[np.logical_and(np.abs(yy)>7, xx>2.5)] = 0.18;


#%% SET SOURCE AND RECEIVERS
AM13=np.loadtxt("AM13.dat")

S = AM13[0:10,0:2:1]
R = AM13[0:10:1,2:4:1]

S = AM13[:,0:2:1]
R = AM13[:,2:4:1]
nd,ndim = R.shape

#%% PLOT MODEL
plt.figure(0)
plt.pcolor(x,y,V)
plt.axes().set_aspect('equal')

for i in range(nd):
    #plt.plot(R[:,0],R[:,1],'v*')
    plt.plot([S[i,0],R[i,0]],[S[i,1],R[i,1]],'w-')
plt.axes().set_aspect('equal')
plt.gca().invert_yaxis()
plt.xlabel('X (m)')
plt.ylabel('Z (m)')
plt.colorbar()
plt.show()



#t = tt.eikonal_traveltime(x,y,[],V,S,R)
t = tt.eikonal_traveltime(x,y,[],V,S,R)
plt.figure(1)
plt.plot(t)
plt.xlabel('Data #')
plt.ylabel('Traveltime (ns)')
plt.show()

