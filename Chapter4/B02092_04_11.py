import sympy
x=sympy.Symbol('x')
a = 1/x + (x*sympy.exp(x) - 1)/x
print(sympy.simplify(a))
print(sympy.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

# exp(x)
# x - 1
