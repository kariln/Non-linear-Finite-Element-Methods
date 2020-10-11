# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:42:22 2020

@author: Kari Ness
central_differences
"""
from numpy import linalg as LA
import numpy as np

def central_differences(K,M,C,D0,dD0):
    #finding eigenvalues w^2 and eigenvectors v
    w, v = LA.eig(K)
    omega = np.sqrt(w)
    T = 2*np.pi/omega
    t0 = 0
    t_end = 5*T[0]
    dt = T[0]/20
    a0 = 1/dt**2
    a1 = 1/(2*dt)
    a2 = 2*a0
    a3 = 1/a2
    
def main():
    k2 = 1
    k1 = 1*10**4
    m1 = 1
    m2 = 1
    K = [[(k1+k2),-k2],[-k2,k2]]
    M = [[m1,0],[0,m2]]
    C = [[0, 0],[0,0]]
    D0 = [1, 10]
    dD0 = [0,0]
    print(central_differences(K,M,C,D0,dD0))
    
main()
    
