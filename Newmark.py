# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:07:25 2020

@author: kariln
Newmark methods
"""
import numpy as np
from numpy import linalg as LA
import abc

class Newmark:
    def __init__(self,gamma, beta, D0, dD0, K, M,C, R_ext):
        self.gamma = gamma
        self.beta = beta
        
        #initial displacement
        self.D0 = D0
        self.D = [D0]
        
        #initial velocity
        self.dD0 = dD0
        self.dD = [dD0]
        
        #acceleration
        self.ddD0 = 
        self.ddD = []
        
        #stiffness matrix
        self.K = K
        
        #mass matrix
        self.M = M
        
        #damping matrix
        self.C = C
        
        #period
        self.T = None
        
        #eigenfrequency
        self.omega = None
        
        #time step
        self.dt = None
        
        self.time_interval =  None
        
        #integration constants
        self.integration_constants = None
        
        #effective stiffness matrix
        self.K_eff = None
        
        #external forces
        self.R_ext = R_ext
        
        #effective load vector
        self.R_eff = None
        
    def get_gamma(self):
        return self.gamma
    
    def get_beta(self):
        return self.beta
        
    def get_K(self):
        return self.K
    
    def get_M(self):
        return self.M
    
    def get_C(self):
        return self.C
    
    def get_D(self):
        return self.D
    
    def get_dD(self):
        return self.dD
    
    def get_ddD(self):
        return self.ddD
    
    def set_eigenfrequency(self):
        #finding eigenvalues w^2 and eigenvectors v
        w, v = LA.eig(self.get_K())
        omega = np.sqrt(w)
        self.omega = omega
        
    def get_eigenfrequency(self):
        return self.omega
        
    def set_period(self):
        T = 2*np.pi/self.get_eigenfrequency()
        self.T = T
        
    def get_period(self):
        return self.T
    
    def set_dt(self):
        dt = self.get_period()[0]/20
        self.dt = dt
        
    def get_dt(self):
        return self.dt
    
    def set_time_interval(self):
        self.time_interval = {'start': 0, 'end': 5*self.get_period()[0]}
        
    def get_start_time(self):
        return self.time_interval()[0]
    
    def get_end_time(self):
        return self.time_interval()[1]
    
    def set_integration_constants(self):
        integration_constants = {}
        gamma = self.get_gamma()
        beta = self.get_beta()
        dt = self.get_dt()
        if gamma >= 0.5 and beta >= 0.25*(0.5+gamma)**2:
            a0 = 1/(beta*dt**2)
            integration_constants.update({'a0':a0})            
            
            a1 = gamma/(beta*dt)
            integration_constants.update({'a1':a1})
            
            a2 = 1/(beta*dt)
            integration_constants.update({'a2':a2})
            
            a3 = 1/(2*beta) -1
            integration_constants.update({'a3':a3})
            
            a4 = gamma/beta -1
            integration_constants.update({'a4':a4})
            
            a5 = dt*(gamma/(2*beta)-1)
            integration_constants.update({'a5':a5})
            
            a6 = dt*(1-gamma)
            integration_constants.update({'a6':a6})
            
            a7 = gamma*dt
            integration_constants.update({'a7':a7})
            
    def get_integration_constants(self):
        return self.integration_constants
    
    def set_K_eff(self):
        a0 = self.get_integration_constants()['a0']
        a1 = self.get_integration_constants()['a1']
        K_eff = a0*self.get_M() + a1*self.get_C() + self.get_K()
        
    def get_K_eff(self):
        return self.K_eff
        
    def get_R_ext(self):
        return self.R_ext
    
    def set_R_eff(self):
        R_ext = self.get_R_ext()
        a0 = self.get_integration_constants()['a0']
        a1 = self.get_integration_constants()['a1']
        a2 = self.get_integration_constants()['a2']
        a3 = self.get_integration_constants()['a3']
        a4 = self.get_integration_constants()['a4']
        a5 = self.get_integration_constants()['a5']
        D = self.get_D()[-1]
        dD = self.get_dD()[-1]
        ddD = self.get_ddD()[-1]
        R_eff = R_ext + M*()
            

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
    R_ext = [[0, 0],[0,0]]
    trapezoidal = Newmark(0.5,0.25, D0, dD0, K, M, C,R_ext)
    damped_newmark = Newmark(0.6,0.3025, D0, dD0, K, M, C,R_ext)

    
main()