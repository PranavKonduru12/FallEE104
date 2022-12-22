from re import X
import pandas as pd
import matplotlib.pyplot as plt # for plotting
import random
import scipy.optimize as opt # will get curve_fit from here
import math

#Plot csv noise wave
axis = ["X", "M"]
df = pd.read_csv("audio_30Hz.csv", usecols=axis)
plt.plot(df.X, df.M)
plt.show()

#Converts csv string columns into floats
df["X"] = pd.to_numeric(df["X"])
#print(df["X"])
df["M"] = pd.to_numeric(df["M"])
#m_float = [float(Y) for Y in axis[1]]

#Plot csv plot through x and y lists to obtain noise 
#xv = [x/100 for x in range(400)] # create x values
xv = df["X"]
#yp = fds(xv,4,1,0.1,1) # perfect y values
yp = df["M"]
yv = [ y+random.gauss(0,0.1) for y in yp] # values with noise
plt.plot(xv,yp,'b')
plt.scatter(xv,yv,alpha=0.3,s=3,c='green')
plt.show()

# first p is the sin multiplier
# second p is the sin phase
# third p is the exponent weight
# fourth is an overall gain factor
def fds(xin,sm,sp,ew,gain):
    return [ gain*math.sin(sm*x+sp)*math.exp(-ew*x) for x in xin]

#noise fit
popt,pcov = opt.curve_fit(fds,xv,yv)
plt.plot(xv,yp,'b')
plt.plot(xv,fds(xv,*popt),'g')
plt.scatter(xv,yv,alpha=0.3,s=3,c='green')
plt.show()

#increase number of data points
xv = [x/100 for x in range(4000)] # create x values
yp = fds(xv,4,1,0.1,1) # perfect y values
yv = [ y+random.gauss(0,0.1) for y in yp] # values with noise
popt,pcov = opt.curve_fit(fds,xv,yv)
yf = fds(xv,*popt) # the fit points for the x values
plt.plot(xv,[abs(yf[ix]-yp[ix]) for ix in range(len(xv))])
plt.show()

#Perfect fit
plt.plot(xv,yp,'g')
plt.scatter(xv,yf,alpha=0.3,s=3,c='red')
plt.show()