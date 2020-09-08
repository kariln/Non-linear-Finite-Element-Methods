# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:16:26 2020

@author: Kari Ness
"""

"""
True Newton-Raphson iteration from initial configuration
"""
import sympy as sy
import pandas as pd

class Iter_info:
    def __init__(self,i, u_i, r_i, tol, kt_i, du_i):
        self.i = i
        self.u = u_i
        self.r = r_i
        self.tol=tol
        self.kt = kt_i
        self.du = du_i
        
    def getInfo(self):
        return [self.i,self.u,self.r,self.tol,self.kt,self.du]
    

#initial conditions
u_i = 0
f_ext = 0.4 #external forces
u = sy.symbols('u')

#defines internal forces and residual function
a = 4
b=-12
c=9
f_int = 0.25*(a*u**3+b*u**2+c*u)
r = f_ext-f_int
kt = sy.diff(-r,u)

#defines tolerance
tol = 10**(-3)

i = 0
r_i = r.subs(u,u_i)
kt_i = kt.subs(u,u_i)
du_i = r_i/kt_i

#declares an empty list
object_list = []
while r_i/f_ext > tol:
    info = Iter_info(i, u_i, r_i, r_i/f_ext, kt_i, du_i)
    object_list.append(info)
    i += 1
    u_i += du_i
    r_i = r.subs(u,u_i)
    kt_i = kt.subs(u,u_i)
    du_i = r_i/kt_i
    
i = []
u_i = []
r_i = []
conv = []
kt = []
du = []
for obj in object_list:
    i.append(obj.getInfo()[0])
    u_i.append(obj.getInfo()[1])
    r_i.append(obj.getInfo()[2])
    conv.append(obj.getInfo()[2]/f_ext)
    kt.append(obj.getInfo()[3])
    du.append(obj.getInfo()[4])



info = {'i':i,
        'u_i': u_i,
        'r_i': r_i,
        'r_i/f_ext' : conv,
        'kt': kt,
        'du':du
        }

df = pd.DataFrame(info, columns = ['i','u_i','r_i','r_i/f_ext','kt','du'])
print(df)
    



    