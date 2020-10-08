# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:16:46 2020

@author: kariln
CENTRAL DIFFERENCE METHOD
"""
import numpy as np

class Central_Differences:
    def __init__(self, dt,t_start,t_end,initial_d,dd0,ddd0):
       self.dt = dt
       self.t_start = t_start
       self.t_end = t_end
       self.initial_d = initial_d
       self.t = np.linspace(t_start,t_end,int((t_end-t_start)/dt))
       self.d = np.zeros(len(self.t))
       self.dd = dd0
       self.ddd = ddd0
       self.d[1] = initial_d
       self.d[0] = self.d[1]-self.dt*self.dd+self.dt**2/2*self.ddd
    
    def get_dt(self):
        return self.dt
    
    def get_d(self):
        return self.d
    
    def get_dd(self):
        return self.dd
    
    def get_ddd(self):
        return self.ddd
    
    def get_d_minus(self):
        return self.get_d()[0]
    
    def set_dd(self, index):
        self.dd = 1/(2*self.get_dt())*(self.get_d()[index]-self.get_d()[index-2])
        
    def set_ddd(self,index):
        self.ddd = 1/self.get_dt()**2*(self.get_d()[index]-2*self.get_d()[index-1]+self.get_d()[index-2])
        
    def set_d(self):
        for i in range(2,len(self.t)):
            self.get_d()[i]= self.get_dt()**2-(self.get_dt()**2-2)*self.get_d()[i-1]-self.get_d()[i-2]

def main():
    #task 11.12.6:
    print("Task a:")
    object = Central_Differences(0.5, 0, 7, 0, 0, 1)
    object.set_d()
    print(object.get_d())
    
    print("Task b:")
    object = Central_Differences(1.0, 0, 7, 0, 0, 1)
    object.set_d()
    print(object.get_d())
    
    print("Task c:")
    object = Central_Differences(2.0, 0, 10, 0, 0, 1)
    object.set_d()
    print(object.get_d())
    
    print("Task d:")
    object = Central_Differences(3.0, 0, 15, 0, 0, 1)
    object.set_d()
    print(object.get_d())
main()