import math
import matplotlib.pyplot as plt # for plotting
import scipy.optimize as opt # will get curve_fit from here

# first p is the sin multiplier
# second p is the sin phase
# third p is the exponent weight
# fourth is an overall gain factor
def fds(xin,sm,sp,ew,gain): # damped sine wave formula
    return [ gain*math.sin(sm*x+sp)*math.exp(-ew*x) for x in xin]

xv = [x/10 for x in range(400)] # create x values
yv = fds(xv,10,4,0.1,1) #Uniquie damped sine wave coefficients 

def polyFit(xvin, yvin):
    popt,pcov = opt.curve_fit(fds,xv,yv)
    print(popt)
    plt.plot(xv,yv,'b')
    plt.plot(xv,fds(xv,*popt),'g')
    plt.show()

def main():
    plt.plot(xv,yv) # plot damped sine wave
    plt.show()
    polyFit(xv, yv) # polyfit for the damped sine wave

main()