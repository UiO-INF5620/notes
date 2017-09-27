# Use functions from appsox1D
from approx1D import *
import os

# want to use symbolic computations
x = sp.Symbol('x')

# Exercise 6
s     = 20
f     = sp.tanh(s*(x - np.pi))
Omega = [0, 2*np.pi]

# Version 1 computing all the coefficients every time
N_max = 10
for N in range(1, N_max):
    psi = [sp.sin((2*i + 1)*x) for i in range(N)]

    u, c = least_squares_orth(f, psi, Omega)

    comparison_plot(f, u, Omega,
                    filename = 'tmp_%04d.png' % N,
                    show=False)
# All files that starts with tmp_
files = 'tmp_*.png'
output = "movie.gif"
# Make a gif
os.system("convert -delay 50 %s %s" % (files, output))

# Version 2 computing only the new coefficient each time
N_max = 10
u = 0
for N in range(0, N_max):
    psi = [sp.sin((2*N + 1)*x)]

    u_new, c_new = least_squares_orth(f, psi, Omega)
    u = u + c_new[0]*psi[0]

    comparison_plot(f, u, Omega, filename = 'tmp2_%04d.png' % N,
                    show=False)
files = 'tmp2_*.png'
output = "movie2.gif"
os.system("convert -delay 50 %s %s" % (files, output))

# Exercise 7
N = 16

# Store the basis functions for a, b and c in a list
psi_list = [[sp.sin((i+1)*x) for i in range(N)],
            [sp.sin((2*i+1)*x) for i in range(N)],
            [sp.sin(2*(i+1)*x) for i in range(N)]]

for psi in psi_list:
    x_L = 0; x_R = 2*np.pi
    B = ((x_R-x)*f.subs(x, x_L) + (x - x_L)*f.subs(x, x_R))/(x_R - x_L)

    # Note that we find the coefiicients for f - B
    # Also, we do the computation non-symbolic since the sylbolic
    # computation takes very long
    u, c = least_squares_orth(f - B, psi, Omega, symbolic=False)
    # And plot u + b, since u only consists
    # of functions that are 0 at the boundary
    comparison_plot(f, u + B, Omega)
