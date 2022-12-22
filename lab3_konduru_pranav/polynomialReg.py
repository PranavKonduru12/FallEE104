# Polynomial plot and fit
# Polynomial equation: y = 10x^3 + 9x^2 + 8x + 7

import numpy as np
import matplotlib.pyplot as plt # for plotting
import warnings

x = np.array([-2, -1, 0, 1, 2]) # X values for 
y = np.array([-53, -2, 7, 34, 139]) # y values
z = np.polyfit(x, y, 3)



def pres(order):    # polynomial fit function that plots a fit over the polynomial
    evres=np.poly1d(np.polyfit(x,y,order)) # creates the polyfit
    ypred = [ evres(v) for v in x]
    plt.plot(x,y,'r',label="orig") # plot original polynomial
    plt.plot(x,ypred,'g',label="pred") # plot fit
    plt.title("fit for order {}".format(order))
    plt.legend()
    plt.show()
    return evres

def main():
    print(z)
    plt.plot(x, y) # plot x and y values 
    plt.show() # displays polynomial
    
    pres(3) # third order polynomial fit

main() # Call multiple calls at once

