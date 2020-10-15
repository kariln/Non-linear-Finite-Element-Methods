# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:43:11 2020

@author: Kari Ness
HHT-alpha method
"""
import newmark

class HHT_alpha(newmark.Newmark):
    def __init__(self,gamma, beta, D0, dD0, K, M,C, R_ext, alpha):
        super().__init__(self,gamma, beta, D0, dD0, K, M,C, R_ext)
    
        self.alpha = alpha
        
    def get_alpha(self):
        return self.alpha

    def set_K_eff(self):
        alpha = self.get_alpha()
        a0 = self.get_integration_constants()['a0']
        a1 = self.get_integration_constants()['a1']
        K_eff = a0*self.get_M() + (1+ alpha)*(a1*self.get_C() + self.get_K())
        
def main():
    k2 = 1
    k1 = 1*10**4
    m1 = 1
    m2 = 1
    K = [[(k1+k2),-k2],[-k2,k2]]
    M = [[m1,0],[0,m2]]
    C = [[0, 0],[0,0]]
    D0 = [[1], [10]]
    dD0 = [[0],[0]]
    R_ext = [[0, 0],[0,0]]
    HHT = HHT_alpha(0.81,0.422, D0, dD0, K, M, C,R_ext,-0.3)
#Lag R_eff, transponere vektorene D, D0, dD0