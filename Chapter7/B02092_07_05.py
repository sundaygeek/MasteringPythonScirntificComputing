import matplotlib.pyplot as plt
from numpy import *
x = linspace(0,10.5,40)
y = linspace(1,8,30)
(X,Y) = meshgrid(x,y)
func = exp(-((X-2.5)**2 + (Y-4)**2)/4) - exp(-((X-7.5)**2 + (Y-4)**2)/4)
contr = plt.contour(x,y,func,colors='r',linewidths=4,
	linestyles='dotted')
plt.clabel(contr)
plt.xlabel("x")
plt.ylabel("y")
plt.show()