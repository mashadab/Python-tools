# Gradient plotting, uses lambda function
# author: Mohammad Afzal Shadab
# date: 05/11/2021

#importing libraries
import numpy as np
import matplotlib.pyplot as plt   #plotting library
from matplotlib import cm         #color map

#some constants
Ks = 0.00944 #cm/s
A  = 1.175e6
gamma = 4.74
alpha = 1.611e6
theta_s = 0.287
theta_r = 0.075
beta    = 3.96

#Constitutive/Anonymous function (one-liner)
Th= lambda h: alpha*(theta_s - theta_r)/(alpha + np.abs(h)**beta)+theta_r #Theta, saturation

#for loading data
data = np.load('Newton_NaturalRichards_cap_grav_eqbm_0.2_2by41_t5000.npz')
zeropt2_sol =data['u_sol']
data = np.load('Newton_NaturalRichards_cap_grav_eqbm_0.4_2by41_t5000.npz')
zeropt4_sol =data['u_sol']
data = np.load('Newton_NaturalRichards_cap_grav_eqbm_0.6_2by41_t5000.npz')
zeropt6_sol =data['u_sol']
data = np.load('Newton_NaturalRichards_cap_grav_eqbm_0.8_2by41_t5000.npz')
zeropt8_sol =data['u_sol']

Blues = cm.get_cmap('Blues', 12)

fig = plt.figure(figsize=(15,7.5) , dpi=100)
plot = plt.plot(np.flip(Yc)[:,0],np.transpose(Th(zeropt2_sol[:,np.shape(zeropt2_sol)[1]-1]).reshape(grid.Nx,grid.Ny))[:,0],c=Blues(0.2),label='0.2%')
plot1 = plt.plot(np.flip(Yc)[:,0],np.transpose(Th(zeropt4_sol[:,np.shape(zeropt4_sol)[1]-1]).reshape(grid.Nx,grid.Ny))[:,0],c=Blues(0.4),label='0.4%')
plot2 = plt.plot(np.flip(Yc)[:,0],np.transpose(Th(zeropt6_sol[:,np.shape(zeropt6_sol)[1]-1]).reshape(grid.Nx,grid.Ny))[:,0],c=Blues(0.6),label='0.6%')
plot3 = plt.plot(np.flip(Yc)[:,0],np.transpose(Th(zeropt8_sol[:,np.shape(zeropt8_sol)[1]-1]).reshape(grid.Nx,grid.Ny))[:,0],c=Blues(0.8),label='0.8%')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.axhline(theta_s,color='k',linestyle='--')
plt.axhline(theta_r,color='k',linestyle='--')
plt.xlim([grid.ymin, grid.ymax])
plt.ylim([0, 0.3])
plt.xlabel(r'Depth, $d$ [cm]')
plt.ylabel(r'Saturation, $\theta$')
plt.legend()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.savefig(f'saturationvsdepth_mixed.pdf',bbox_inches='tight', dpi = 600)