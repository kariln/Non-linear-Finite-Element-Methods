# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:55:30 2020

@author: Kari Ness
"""
"""
Newton-Raphson method (N-R)
"""
 
import sympy

#code terminates based on number of iterations
def iterations(num_it,f,D,P,d):
    #current iteration,i
    i = 0;
    while i < num_it:
        deltaD = NewtonRaphson(f,D,P,d);
        d = d+deltaD;
        i += 1;
    return float(d)
    
#code terminates based on tolerance    
#def tolerances(tolerance):

def NewtonRaphson(f,D,P,d):        
    #finds residual
    r = P-f;
    
    #numerical values of r
    r_num = r.subs({D:d});
    
    #derivative of residual, drdd
    drdd = sympy.diff(r,D);
    
    #finds tangent stiffness
    Kt = -drdd.subs({D:d});
    print(Kt)
    
    #finds deltaD
    deltaD = r_num/Kt;
    
    return deltaD

def main():
    D = sympy.Symbol('D')
    f = 5*D-4*D**2;
    #Target value, P
    P = 1; 
    #dependent variable, d
    d = 0;
    num_it = 5;
    print(iterations(num_it,f,D,P,d))
main() 