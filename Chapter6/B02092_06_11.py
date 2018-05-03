from sympy import diff, symbols, Symbol, exp, dsolve, subs, Function
from sympy import *
diff(x**4, x)
diff( x**3*cos(x), x )
diff( cos(x**2), x )
diff( x/sin(x), x )
diff(x**3, x, 2)
diff( exp(x), x)

x = symbols('x')
f = symbols('f', cls=Function) 
C1= sym
dsolve( f(x) - diff(f(x),x), f(x) )

#The boundary conditions are passed to dsolve as a dictionary, through the ics named argument.
from sympy import *
x=symbols('x')
f=symbols('f', cls=Function)
dsolve(Eq(f(x).diff(x,x), 900*(f(x)-1+2*x)), f(x), ics={f(0):5, f(2):10})
#f(x) = C1*e^−30x + C2*e^30x − 2x + 1

x = Symbol('x')
f = 4*x**3-3*x**2+2x
diff(f, x)
sols = solve( diff(f,x), x)
sols
diff(diff(f,x), x).subs( {x:sols[0]} )
diff(diff(f,x), x).subs( {x:sols[1]} )
