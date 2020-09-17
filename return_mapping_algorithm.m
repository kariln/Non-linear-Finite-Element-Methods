clear all
close all
clc

A=1;
L=5;
E=200000;%elastic modulus
yield_stress=200;
Kmod=2000; %Plastic modulus
Hmod=4000;%kinematic hardening modulus
ypsilon = 0.3; %poisson's ratio

alpha0=0;
gamma0=0;

u=[0:0.001:0.05 0.049:-0.001:-0.05 -0.049:0-001:0.05 0.049:-0.001:-0.05];

%preallocates memory for epsilon, epsilon_p, plastic multiplier, alpha,
%gamma
epsilon = zeros(1,length(u)); %total strain
epsilon_p = zeros(1,length(u)); %plastic strain
alpha = zeros(1,length(u)); %Kinematic strain hardening parameter
gamma = zeros(1,length(u)); %Plastic multiplier - Internal hardening variable connected with isotropic haredning 

for t=1:length(u)
    epsilon(t)=u(t)/L;
    
    if t==1
        stress_trial = E*epsilon(t);
        F_trial = abs(stress_trial-alpha0)-(yield_stress+Kmod*gamma0);
    else
        stress_trial = E*(epsilon(t)-epsilon_p(t-1));
        F_trial = abs(stress_trial-alpha(t-1))-(yield_stress+Kmod*gamma(t-1));
    end
    
    if F_trial <= 0 %F = 0 plastic, F<0 elastic, F>0 not legal
       stress = stress_trial;
       if t == 1
           epsilon_p(t) = 0;
       else
          epsilon_p(t) =  
       end
    end
    
    
end