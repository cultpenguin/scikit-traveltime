import numpy as np
import pylab as plt
from traveltime import eikonal_traveltime


#%% TRAVELTIME S-R
nr=14;
ns=1;
x_rec=5*np.ones([nr])
y_rec = np.linspace(1, 12,nr);
R=np.array([x_rec,y_rec]).transpose()
S=np.zeros_like(R)
S[:,0]=0;
S[:,1]=5;


plt.pcolor(x,y,t_map[0])
for i in range(nr):
    #plt.plot(R[:,0],R[:,1],'v*')
    plt.plot([S[i,0],R[i,0]],[S[i,1],R[i,1]],'k-')
plt.axes().set_aspect('equal')
plt.show()

t = eikonal_traveltime(x,y,[],V,S,R)
plt.plot(R[:,1],t,'-*')
plt.show()
