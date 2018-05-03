import sympy
x = sympy.Symbol('x')
temp = sympy.integrate(x**3 + 2*x**2 + x, x)
print(temp)
temp = sympy.integrate(x/(x**2+2*x), x)
print(temp)


# x**4/4 + 2*x**3/3 + x**2/2
# log(x + 2)
