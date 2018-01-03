# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:10:11 2017

@author: thoma
"""

import numpy as np
import pylab as plt
import skfmm

'''
eikonal: simple wrappwe for skfmmm using as single source
'''
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



'''
eikonal_traveltime: simple wrappwe for skfmmm using as single source
'''
def eikonal_traveltime(x=[],y=[],z=[],V=[],S=[],R=[]):
    import numpy as np
    #import skfmm
    from scipy import interpolate
        

    nr, ndim = np.atleast_2d(R).shape
    ns, ndim = np.atleast_2d(S).shape

    if ((ns==nr)&(ns>1)):
        print('More than one set of sources and receivers (ns=nr=%d). using eikonal_traveltime_mul instaed' % ns)
        t = eikonal_traveltime_mul(x,y,z,V,S,R)    
        return t
        

    if (ns>1):
        print('Number for sources larger than 1(ns=%d)! use eikonal_traveltime_mul instead' % ns)

    
    t=np.zeros(nr)
    #phi = -1*np.ones_like(V)    

    #i_source = 0;
    #t_map = eikonal(x,y,z,V,S[i_source,:])
    t_map = eikonal(x,y,z,V,S)

    if ndim==2:   
        f = interpolate.interp2d(x, y, t_map, kind='cubic');
        tt = f(R[:,0].transpose(),R[:,1].transpose())
        for i in range(nr):
            Rx=R[i,0]
            Ry=R[i,1]
            tt=f(Rx,Ry)
            t[i]=tt[0]
            
    return t
    

'''
eikonal_traveltime: simple wrappwe for skfmmm using multiple sources
'''
def eikonal_traveltime_mul(x=[],y=[],z=[],V=[],S=[],R=[]):
    
    nr, ndim = R.shape
    ns, ndim = S.shape

    
    # Check that S and R have the same size
    if (ns != nr):
        print('Number for sources and receivers is not the same(ns=%d, nr=%d)! ' % (ns,nr))
    
    t=np.zeros(nr)
    
    
    # Find unique sources 
    Su=np.unique(S, axis=0)
    nsu,ndim = Su.shape
    # print('Number for unique source locations is %d (out of %d sources). ' % (nsu,ns))
        
    for i in range(nsu):
        # print('working with source %03d/%03d, at location [%4g,%4g]' % (i+1,nsu,Su[i,0],Su[i,1]))
        
        Srow = Su[i,0:2]
    
        # findo matching rows
        dummy=np.where(np.all(Srow==S,axis=1))
        i_index = dummy[0]
    
        t_i = eikonal_traveltime(x,y,z,V,Srow,R[i_index,:])
        
        # update traveltime 
        t[i_index] = t_i

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
