# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:16:46 2020

@author: kariln
CENTRAL DIFFERENCE METHOD
"""
import numpy as np
from newmark import Newmark

class Central_Differences(Newmark):
    def __init__(self, D0, dD0, K, M,C, R_ext):
        super().__init__(self,gamma, beta, D0, dD0, K, M,C, R_ext)
        
    def set_integration_constants(self):
        integration_constants = {}

        dt = self.get_dt()

        a0 = 1/dt**2
        integration_constants.update({'a0':a0})  
        
        a1 = 1/(2*dt)
        integration_constants.update({'a1':a1})
        
        a2 = 2*a0
        integration_constants.update({'a2':a2})
        
        a3 = 1/a2
        integration_constants.update({'a3':a3})

    def set_K_eff(self):
        a0 = self.get_integration_constants()['a0']
        a1 = self.get_integration_constants()['a1']
        K_eff = a0*self.get_M() + a1*self.get_C()
        
        #Lag R_eff

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
    central_difference = Central_Differences(0.5,0, D0, dD0, K, M, C, R_ext)
main()