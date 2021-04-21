"""
Newton-Raphson iteration for a system of nonlinear algebraic equation
author: Mohammad Afzal Shadab
email: mashadab@utexas.edu
"""

import numpy as np

#residual
res = lambda u:  np.array([3.0*u[0] - 2.0*np.sqrt(u[1]*u[2]), \
                           u[1]**2.0/2.0 + u[0]*np.exp(u[1])+5.0*u[2],\
                           u[0]-4.0*u[1]+4.0*u[2]])
  
#analytical Jacobian  
Jac = lambda u:  np.array([[3.0,-(u[2]/u[1])**(1/2),-(u[1]/u[2])**(1/2)],\
                           [np.exp(u[1]),u[1]+u[0]*np.exp(u[1]),5],\
                           [1.0,-4.0,4.0]]) 

u = np.array([1,2,3])  #initial guess  
max_iter = 20                            #maximum number of iteration
tol      = 1e-5                          #tolerance on the norm of du

i=1
du = 1
while True:
    if i< max_iter and np.linalg.norm(du)>tol:
        du = -np.linalg.solve(Jac(u),res(u))
        u  =  u + du
        print('iter',i,'u',u,'\n','du',du)
    
    elif i==max_iter and np.linalg.norm(du)>tol:
        print(f'Error: Newton did not converge in {max_iter} steps!')
        break
    
    else:
        print(f'Success: Newton converged in {i} steps!')
        break        
        
    i+=1
    
    
    



