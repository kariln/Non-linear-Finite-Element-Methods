clear all
close all
clc

A=1;
L=5;
E=200000;%elastic modulus
yield_stress=200;
Kmod=2000; %Plastic modulus
Hmod=4000;%kinematic hardening modulus

alpha0=0;
gamma0=0;

u=[0:0.001:0.05 0.049:-0.001:-0.05 -0.049:0-001:0.05 0.049:-0.001:-0.05];

%preallocates memory for epsilon, epsilon_p, plastic multiplier, alpha,
%gamma
epsilon = zeros(1,length(u)); %total strain
epsilon_p = zeros(1,length(u)); %plastic strain
lambda = zeros(1,length(u)); %plastic multiplier
alpha = zeros(1,length(u)); %Kinematic strain hardening parameter
gamma = zeros(1,length(u)); %Internal hardening variable connected with isotropic haredning 

for t=1:length(u)
    epsilon(t)=u(t)/L;
    
    if t==1
        stress_trial = E*epsilon(t);
    else
        stress_trial = E*(epsilon(t)-epsilon_p(t-1));
    end
    
    F_trial = 
end