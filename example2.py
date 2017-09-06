import numpy as np
import sympy as sym
x = sym.symbols('x')

def example(a, b, c):
    return a + b + c

def test_something():
    a = 1; b = 2; c = 3
    expected = 6
    computed = example(a, b, c)
    sucess = abs(expected - computed) < 1E-5
    assert sucess

def test_multiple():
    n = 4
    expected = range(6, 6+n)
    for i in range(n):
        a = 1 + i; b = 2; c= 3
        computed = example(a, b, c)
        sucess = abs(expected[i] - computed) < 1E-5
        assert sucess

def test_numpy_array():
    t = np.linspace(0, 10, 101)
    f = x**2
    df = sym.diff(f, x)
    # make a python function of the derivative, and evaluate at all points t
    y = sym.lambdify(x, df)(t)
    y_exact = 2*t
    sucess = np.all(np.absolute(y - y_exact) < 1E-5)
    msg = "the value is wrong"
    assert sucess, msg

# Example run:
# Termina> nosetests example2.py
# It is also possible to use other test programs than nosetests
# for example pytest. See http://docs.python-guide.org/en/latest/writing/tests/

