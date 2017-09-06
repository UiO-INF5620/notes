import sympy as sym

A, B, C, x = sym.symbols('A B C x')

f = A*x**2 + B*x + C
print f
print f.subs(x, 1)
g = lambda t: A*t + B
# EQuivalent to
#def g(t):
#    return A*t + B

print g(x)
print g(x).subs({A:1, B:2, x:3})
h = sym.lambdify(x, x**2)
print h(2)

print sym.diff(f, x)
print sym.diff(f, x, 3)
print sym.integrate(f, x)
print sym.integrate(f, (x, -1, 1))
print sym.integrate(sym.exp(-x), (x, 0, sym.oo))

print sym.series(f, x, x0=0, n=4)
print sym.series(sym.exp(x), x, x0=0, n=4)

print sym.solve(f, x)
print sym.solve(x+1, x)
print sym.solve([A+B, A-B+1], [A, B])
print sym.factor(x**2 + 2*x + 1)

m = sym.Matrix([[A, B], [x, C]])
print m**2

