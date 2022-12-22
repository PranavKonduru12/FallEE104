import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math

#plot multiple variables
x0 = [x/10 for x in range(100)]
x1 = [math.sin(x**2) for x in range(100)]
xa=(x0,x1)

#Function of the two variables
def rf(X,fx0,fx1):
    x0,x1=X
    rv=np.sin(np.multiply(x0,fx0)+np.sin(np.multiply(x1,fx1)))
    return rv

yv = rf((x0,x1),2,3)

#Curve fit tests
def with_hint(h0, h1):
    popt,pcov=opt.curve_fit(rf,xa,yv,(h0,h1)) # Polynomial fit
    #print(popt)
    #print(pcov)
    plt.plot(rf((x0,x1),2,3),'b') # original polynomial
    plt.plot(rf((x0,x1),*popt),'g') # Plot of the polyfit
    plt.show()

def main():
    plt.plot(yv) # Plot of the rf function
    plt.show()

    with_hint(0,0) # peaks and valleys are too low compared to the orignial polynomial
    with_hint(1, 1) # Some of the peaks and valleys match but are off phase to the right
    with_hint(1, 2) # All magnitue of peaks and valleys match but off phase
    with_hint(2, 1) # Majority of the fit is on the polynomial
    with_hint(2, 3) # curve fit matches

main()