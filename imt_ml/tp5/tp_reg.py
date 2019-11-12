# Libraries: Standard ones
import numpy as np
import matplotlib.pyplot as plt



# seed the pseudorandom number generator to reproduce results
from numpy.random import seed
from numpy.random import randn
from numpy.random import uniform


# input size
N = 100


# seed the pseudorandom number generator
seed(1255)

# generate random data in which y is a noisy function of x
x = uniform(-5,5,N)

y = x + randn(N) + 3 

xplot = np.linspace(-5,5,N);
plt.plot(x,y,"o")
plt.ylabel("y")
plt.xlabel("x")
plt.title("y is a noisy function of x")
#plt.show()



# Matrix of predictors
x_m = np.copy(x)

# Add column of 1s for intercept coefficient
intercept = np.ones(N)

xx = np.concatenate((intercept[np.newaxis,:],x_m[np.newaxis,:]),axis=0)
xx = np.transpose(xx)


# Initialise w matrix
w = 0.1 * randn(np.shape(xx)[1]);
w = w[np.newaxis,:];
w = np.transpose(w)



print("xshape=",np.shape(x))
print("yshape=",np.shape(y))

nb_epoch = 200
lr = 0.01


y = y[np.newaxis,:];
y = np.transpose(y)


for i in range(nb_epoch):
    err = np.dot(xx,w) - y
    delta = np.dot(np.transpose(xx),err) * 2/N
    #print("delta=",delta)
    w = w - lr*delta
    #print(w)


aline=w[0]+w[1]*xplot
print(aline)
plt.plot(xplot,aline,xplot,x,xplot,y)
residus = np.dot(xx,w) - y
plt.plot(x,err,"o")
plt.show()



