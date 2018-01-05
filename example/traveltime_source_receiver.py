import numpy as np
import pylab as plt
import traveltime as tt

plt.ion(), 

#%% CREATE REFERENCE VELOCITY MODEL
dx=0.2;
x = np.arange(-0.4,5.401,dx)
y = np.arange(0.6,12.401,dx)

#x = np.linspace(-0.4,5.4,30);
#y = np.linspace(0.6,12.4,60);

xx,yy = np.meshgrid(x,y)
V = 0.1*np.ones_like(xx);
#V[yy>6] = 0.15;
#V[np.logical_and(np.abs(yy)>7, xx>2.5)] = 0.18;


#%% Load the source and receiver locations, and velocity field

AM13=np.loadtxt("AM13_SR_traveltime.dat")
nd,nc=AM13.shape
i_use = np.arange(0,nd,1) # use a subset of the 'nd' data
#i_use = np.arange(0,nd,5)
#i_use = np.arange(0,30,1)
S = AM13[i_use,0:2:1]
R = AM13[i_use,2:4:1]

#S = AM13[:,0:2:1]
#R = AM13[:,2:4:1]
nd,ndim = R.shape

# Load a velocity field
V=np.loadtxt("AM13_V.dat")
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
plt.plot(i_use,AM13[i_use,9], label='Matlab FMM')
#plt.plot(i_use,AM13[i_use,5])
#plt.plot(i_use,AM13[i_use,6])
plt.plot(i_use,t,  label='scikit-traveltime')
plt.legend()
plt.xlabel('Data #')
plt.ylabel('Traveltime (ns)')
plt.show()
