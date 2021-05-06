
"""
Newton-Raphson iteration
author: Mohammad Afzal Shadab
email: mashadab@utexas.edu
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#Trying to find root of the equation exp(x) = 2, correct answer is x=0.6931

res = lambda x: np.exp(x) - 2.0 #Residual of the function
jac = lambda x: np.exp(x)       #Jacobian
iter_max = 20                   #Maximum iteration
x = 1.0                         #Initial guess

# (a) For running till maximum iteration
plt.figure()
plt.ylabel('x')
plt.xlabel('iterations')
for i in range(iter_max):
    
    dx = -res(x)/jac(x)
    x  = x+dx
    plt.plot(i,x,'ro')
    print(i)

# (b) For controlled stop using norms
tol = 1e-5
x   = 1.0
dx  = 1.0

plt.figure()
plt.ylabel('x')
plt.xlabel('iterations')

i = 0
while True:
    i = i + 1
    if np.linalg.norm(dx)>tol and i<iter_max:
        dx = -res(x)/jac(x)
        x  = x+dx
        plt.plot(i,x,'bo')
        print(i)
    elif np.linalg.norm(dx)>tol and i==iter_max:
        print('Newton has not converged')
        break
    else:
        print(f'Newton has converged in {i} iterations.') 
        break
        
# (c) Using fsolve
x0 = 100
x   = fsolve(res, x0)
print(f'fsolve answer: {x}.') 
