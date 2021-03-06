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

%initial conitions
alpha0=0;
gamma0=0;

u=[0:0.001:0.05 0.049:-0.001:-0.05 -0.049:0-001:0.05 0.049:-0.001:-0.05];

%preallocates memory for epsilon, epsilon_p, plastic multiplier, alpha,
%gamma
epsilon = zeros(1,length(u)); %total strain
epsilon_p = zeros(1,length(u)); %plastic strain
alpha = zeros(1,length(u)); %Kinematic strain hardening parameter
gamma = zeros(1,length(u));  % Internal hardening variable connected with isotropic haredning 
sigma = zeros(1,length(u)); %stress

for t=1:length(u)
    epsilon(t)=u(t)/L;
    
    %Computes the trial elastic state by assuming the material response is
    %purely elastic when applying d_epsilon.
    if t==1
        sigma_trial = E*epsilon(t);
        F_trial = abs(sigma_trial-alpha0)-(yield_stress+Kmod*gamma0);
    else
        sigma_trial = E*(epsilon(t)-epsilon_p(t-1));
        F_trial = abs(sigma_trial-alpha(t-1))-(yield_stress+Kmod*gamma(t-1));
    end
    
    if F_trial <= 0 %elastic step,F = 0 plastic, F<0 elastic, F>0 not legal
       sigma(t) = sigma_trial;
       if t == 1
           %initial condition: no plastic strain
           epsilon_p(t) = 0;
       else
           %as elastic step, epsilon_p is the same as previous stage
          epsilon_p(t) = epsilon_p(t-1);  
       end
    else %plastic step, F_trial > 0, plastic multiplier, d_gamma >0
        if t == 1
            gamma(t) = gamma0;
            epsilon_p(t) = 0;
            sigma(t) = sigma_trial;
            alpha(t) = alpha0;
        else
            d_gamma = F_trial/(E+(Kmod+Hmod));
            sigma(t) = sigma_trial - d_gamma*E*sign(sigma_trial-alpha(t-1));
            epsilon_p(t) = epsilon_p(t-1) + d_gamma*sign(sigma_trial-alpha(t-1));
            alpha(t) = alpha(t-1)+d_gamma*Hmod*sign(sigma_trial-alpha(t-1));
            gamma(t) = gamma(t-1) + d_gamma;
        end
    
    end  
end
force = sigma*A;
figure(1)
plot(force,u)
xlabel('Force, N')
ylabel('Displacement, u')

figure(2)
plot(epsilon,sigma)
xlabel('Strain')
ylabel('Stress')

figure(3)
plot(epsilon_p)
ylabel('plastic strain')

figure(4)
plot(gamma)
ylabel('Plastic multiplier')