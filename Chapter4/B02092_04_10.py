import sympy
a=sympy.Symbol('a')
b=sympy.Symbol('b')
e=(a+b)**4
print e
print e.expand()

# (a + b)**4
# a**4 + 4*a**3*b + 6*a**2*b**2 + 4*a*b**3 + b**4