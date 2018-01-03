# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:10:11 2017

@author: thoma
"""

import numpy as np
import pylab as plt
import skfmm


def eikonal(x=[],y=[],z=[],V=[],S=[]):
    import numpy as np
    import skfmm
    
    t=[];

    dx = float(x[1]-x[0])
    phi = -1*np.ones_like(V)    

    if S.ndim==1:
        S=np.array([S]);
        ns=1
        ns, ndim = S.shape
    else:
        ns, ndim = S.shape

    for i in range(ns):
        # get location of source
        #print(i)
        ix = np.abs(x-S[i,0]).argmin();
        if ndim>1:
            iy = np.abs(y-S[i,1]).argmin();
        if ndim>2:
            iz = np.abs(z-S[i,2]).argmin();
    
        if ndim>2:
            phi[iy,ix,iz]=1;    
        elif ndim>1:
            phi[iy,ix]=1;    
        else:
            phi[ix]=1;
    
        t_comp = skfmm.travel_time(phi, V, dx)
    
        t.append(t_comp)
    
    return t



def eikonal_traveltime(x=[],y=[],z=[],V=[],S=[],R=[]):
    import numpy as np
    import skfmm
    from scipy import interpolate
    
    
    phi = -1*np.ones_like(V)    

    nr, ndim = R.shape
    t=np.zeros(nr)


    i_source = 0;
    t_map = eikonal(x,y,z,V,S[i_source,:])

    if ndim==2:   
        f = interpolate.interp2d(x, y, t_map, kind='cubic');
        tt = f(R[:,0].transpose(),R[:,1].transpose())
        for i in range(nr):
            Rx=R[i,0]
            Ry=R[i,1]
            tt=f(Rx,Ry)
            t[i]=tt[0]
            
    return t
    

def example_map():
    
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
        #plt.plot(R[:,0],R[:,1],'k*')
        plt.plot([S[i,0],R[i,0]],[S[i,1],R[i,1]],'k-')
    plt.axes().set_aspect('equal')
    plt.show()

    t = eikonal_traveltime(x,y,[],V,S,R)
    plt.plot(R[:,1],t,'-*')
    plt.show()
