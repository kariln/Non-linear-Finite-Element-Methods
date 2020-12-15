# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 11:55:30 2020

@author: Kari Ness
"""
"""
Newton-Raphson method (N-R)
"""
 
import sympy
import numpy as np
import matplotlib.pyplot as plt


#code terminates based on number of iterations
def iterations(num_it,f,D,P,d):
    table = np.zeros((num_it,6))
    #current iteration,i
    i = 0;
    while i < num_it:
        #iteration in table
        table[i,0] = i
        deltaD,Kt,r_num = NewtonRaphson(f,D,P,d);
        #displacement in table
        table[i,1]=d
        #deltaD in table
        table[i,5] = deltaD
        #Kt in table
        table[i,4] = Kt
        #residual in table
        table[i,2] = r_num
        #convergence criteria
        table[i,3] = r_num/P
        d = d+deltaD;
        i += 1;
    print(table)
    return table
    
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
    
    #finds deltaD
    deltaD = r_num/Kt;
    
    return deltaD,Kt,r_num

def plot_eq_path(f,table,D):
    drdd = sympy.diff(f,D);
    
    d = np.linspace(table[0,1],table[-1,1]*12,100)
    
    f_num = []
    Kt = []
    
    for i in range(0,100):
        f_num.append(f.subs({D:d[i]}));
        Kt.append(drdd.subs({D:d}))

    plt.plot(d,f_num)
    limit_points = sympy.solve(Kt, D)
    print('Limit points: ')
    for i in range(len(limit_points)):
        print(str(limit_points[i][0]) + ','+ str(f.subs({D:limit_points[i][0]})))
    
    zero_points = sympy.solve(f, D)
    print('Zero points: ' + str(zero_points))
    
    


def main():
    D = sympy.Symbol('D')
    f = 1/2*(2*D-3*D**2+D**3);
    #Target value, P
    P = 0.125; 
    #dependent variable, d
    d = 0;
    num_it = 5;
    table = iterations(num_it,f,D,P,d)
    plot_eq_path(f,table,D)
main() 