#Using vectorized boolean based function to evaluate phase behavior of three phase mixture: ice (solid), water (liquid), and gas
import numpy as np

# author: Mohammad Afzal Shadab
# date: 02/05/2021
# Description:
# This file contains enthalpy conversions to and from Temperature or phi for three phase: ice, water and gas
# Input: Enthalpy (H) and volume fraction of gas (phi_g) since gas is inert
# Output: Water, ice volume fraction and Temperature
# Parameters: Rest Tm,rho_i,rho_w,rho_g,cp_i,cp_w,cp_g and Latent heat of fusion L

def eval_phase_behavior(H,Tm,rho_i,rho_w,rho_g,cp_i,cp_w,cp_g,phi_g,L):
    N     = len(H)          #length of enthalpy vector

    field = np.zeros((N,1)) #initializing indicator of the phases: 1 - gas + ice, 2 - gas + water + ice, 3 - ice + gas

    #Thresholding field on the basis of Enthalpy H
    field[H <= (1 - phi_g)*rho_w*L]=2          #Regime 2: gas + ice + water
    field[H <= 0]=1                            #Regime 1: gas + ice
    field[H > (1 - phi_g)*rho_w*L]=3           #Regime 3: gas + water

    #print('Field',field)

    #output vectors    
    phi_w = np.zeros((N,1)) #initializing water volume fraction vector N by 1
    phi_i = np.zeros((N,1)) #initializing water volume fraction vector N by 1
    T     = np.zeros((N,1)) #initializing Temperature vector N by 1
    
    #Regime 1: Ice and gas
    #Volume fraction
    phi_i[field==1] = 1.0 - phi_g[field==1]

    #Temperature
    T[field==1] = Tm + H[field==1]/(phi_i[field==1]*rho_i*cp_i + phi_g[field==1]*rho_g*cp_g)

    #Regime 2: Ice, Wwter and gas
    #Volume fraction
    phi_w[field==2] = H[field==2]/(rho_w * L)
    phi_i[field==2] = 1.0 - phi_w[field==2]

    #Temperature
    T[field==2] = Tm

    #Regime 3: Water and gas
    #Volume fraction
    phi_w[field==3] = 1.0 - phi_g[field==3]

    #Temperature
    T[field==3] = Tm + H[field==3]/(phi_w[field==3]*rho_w*cp_w + phi_g[field==3]*rho_g*cp_g)

    return phi_w,phi_i,T;

#For initializing
def enthalpyfromT(T,Tm,rho_i,rho_w,rho_g,cp_i,cp_w,cp_g,phi_w,phi_g,L):
    H = np.zeros_like(T)   

    for i in range(0,len(T)):
        if T[i,0] < Tm:
            H[i,0] = (rho_i*cp_i*(1.0 - phi_g[i,0]) + rho_g*cp_g*phi_g[i,0]) * (T[i,0] - Tm) 

        elif T[i,0] == Tm:
            H[i,0] = phi_w[i,0]*rho_w*L 

        else:
            H[i,0] = (rho_w*cp_w*(1.0 - phi_g[i,0]) + rho_g*cp_g*phi_g[i,0]) * (T[i,0] - Tm) + (1.0 - phi_g[i,0])*rho_w*L     
    return H;