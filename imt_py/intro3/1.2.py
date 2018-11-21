from numpy import *
import matplotlib.pyplot as plt

x=linspace(0,2*pi,43)
y=cos(x)
yb=sin(x)
l1,l2=plt.plot(x,y,"b",x,yb,"r")
plt.title("Cosine and sine functions")
plt.legend(("cos","sin"))
plt.figure(2)
xx=linspace(-4,4,50)
yy=1/(1+xx**2)
plt.plot(xx,yy,"g")
plt.title("Runge function")
plt.legend(["$1/(1+x^2)$"])
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()