# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:03:58 2020

@author: Kari Ness
"""

"""
Euler's method
"""
import pandas as pd
import numpy as np

def Euler(x0,y0,dx,dydx0,xn):
     x = x0;
     y = y0;
     dydx = dydx0;
     N = int((xn-x0)/dx);
     results = np.zeros((3,N)); #preallocates space for the data
     results[0,0] = x;
     results[1,0] = y;
     results[2,0] = dydx;
     
     for i in range(1,N):
         x += dx;
         results[0,i] = x;
         y += dydx*x
         results[1,i] = y;
         dydx = (results[1,i]-results[1,i-1])/(results[0,i]-results[0,i-1])         
         results[2,i] = dydx;
         

         
     #creating dataframe to display table nicely
     data = {'x':results[0,:],'y':results[1,:],'dydx':results[2,:]}
     df = pd.DataFrame (data, columns = ['x','y','dydx'])
     print (df)
     return df
 
def main():
    Euler(1,0.1111,2,0.2469,9)
main()
         
         
     