import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
import ctypes
import os
import sys

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ + O)
	return x_circ
	
def contact(V,u,f,h):
    #intermediate
    gh = h.T@V@h+2*u.T@h+f 
    
    #matrix of tangents
    sigmat = (V@h+u)@(V@h+u).T-gh*V
    
    
    #Spectral decomposition
    D, P = LA.eig(sigmat)
    
    u1 = np.array(([np.sqrt(np.abs(D[1])),np.sqrt(np.abs(D[0]))]))
    u2 = np.array(([np.sqrt(np.abs(D[1])),-np.sqrt(np.abs(D[0]))]))
    
    u1 = u1.reshape(-1,1)
    u2 = u2.reshape(-1,1)
    
    #direction vectors
    m1 = P@u1
    m2 = P@u2
    #print(m1,m2)
    # Converting 1D array to a 2D numpy array of incompatible shape will cause error
    m1= np.reshape(m1, (2, 1))
    m2= np.reshape(m2, (2, 1))
    mu1 = -(m1.T@(V@h+u))/(m1.T@V@m1)
    mu2 = -(m2.T@(V@h+u))/(m2.T@V@m2)
    #print(mu1,mu2)
    x1 = h + mu1*m1
    x2 = h + mu2*m2
    return(x1,x2)
    
def circ_param(u,f):
    O = -u
    r = np.sqrt(LA.norm(u)**2-f)
    return O,r

V = np.array([[1, 0], [0, 1]])
u = np.array([-3, -2])
f = 4

h = np.array([0, 0]).reshape(-1, 1)

center, radius = circ_param(u, f)

circle_points = circ_gen(center.reshape(-1, 1), radius)

P1, P2 = contact(V, u.reshape(-1, 1), f, h)

plt.figure(figsize=(8, 8))

plt.plot(circle_points[0, :], circle_points[1, :], label=r'$x^2+y^2-6x-4y+4=0$')

plt.plot([h[0,0], P1[0,0]], [h[1,0], P1[1,0]], 'r-', label='Tangent 1')
plt.plot([h[0,0], P2[0,0]], [h[1,0], P2[1,0]], 'g-', label='Tangent 2')

plt.plot(center[0], center[1], 'ko', label=f'Center ({center[0]:.0f}, {center[1]:.0f})')
plt.plot(h[0, 0], h[1, 0], 'o', color='purple', label='O (0, 0)')
plt.plot(P1[0, 0], P1[1, 0], 'ro', label=fr' $\vec{P1}$ ({P1[0,0]:.2f}, {P1[1,0]:.2f})')
plt.plot(P2[0, 0], P2[1, 0], 'go', label=fr' $\vec{P2}$ ({P2[0,0]:.2f}, {P2[1,0]:.2f})')

plt.title("Circle with Centre (3,2) and Its Tangents from Origin")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axhline()
plt.axvline()
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')

plt.savefig("../figs/plot_p.jpg", bbox_inches='tight')
plt.show()
