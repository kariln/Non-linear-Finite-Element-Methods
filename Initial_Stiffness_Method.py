# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:26:31 2020

@author: Kari Ness
"""

"""
Initial stiffness method-the same tangent stiffness Kt is used in all iterations.
"""

import sympy

#code terminates based on number of iterations
def iterations(num_it,f,D,P,d):
    #current iteration,i
    i = 0;
    #residual function
    r = P-f;
    #derivative of residual, drdd
    drdd = sympy.diff(r,D);
    #finds tangent stiffness
    Kt = -drdd.subs({D:d});
    while i < num_it:
        deltaD = NewtonRaphson(f,D,P,d, Kt);
        d = d+deltaD;
        i += 1;
    return float(d)
    
#code terminates based on tolerance    
#def tolerances(tolerance):

def NewtonRaphson(f,D,P,d,Kt):        
    #finds residual
    r = P-f;
    
    #numerical values of r
    r_num = r.subs({D:d});
    
    #finds deltaD
    deltaD = r_num/Kt;
    
    return deltaD

def main():
    D = sympy.Symbol('D')
    f = 10*D/(D+1);
    #Target value, P
    P = 8; 
    #dependent variable, d
    d = 0;
    num_it = 5;
    print(iterations(num_it,f,D,P,d))
main() 