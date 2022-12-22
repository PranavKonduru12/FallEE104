#http://apmonitor.com/che263/index.php/Main/PythonDynamicSim
import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#def tank(h,t, c1, c2, bed, nurse, doc, equip):
def tank(h,t):
   # constants
   #c1 = 0.13
   #c2 = 0.009
   c1 = 30
   c2 = 5
   beds_er = 30
   beds_icu = 10
   nurses = 2
   doctors = 1
   equipment = 2 # medical equipment
   Ac = beds_er * (nurses + doctors + equipment)  # m^2 (number of beds) Hospital occupancy
   Ai = beds_icu * (nurses + doctors + equipment)
   # inflow
   qin = 40   # m^3/hr # number of people coming into the ER
   #qin = 50
   # outflow
   qout1 = c1 * h[0]**0.5 # rate of people leaving ER
   qout2 = c2 * h[1]**0.5 # rate of people laving ICU
   # differential equations
   dhdt1 = (qin   - qout1) / Ac
   dhdt2 = (qout1 - qout2) / Ai
   # overflow conditions
   if h[0]>=1 and dhdt1>=0:
       dhdt1 = 0
   if h[1]>=1 and dhdt2>=0:
       dhdt2 = 0
   dhdt = [dhdt1,dhdt2]
   return dhdt

# integrate the equations
t = np.linspace(0,10) # times to report solution
h0 = [0,0]            #initial conditions for height
#c = (3, 2)   #constants
#factors = (beds, nurses, docs, equipment)
y = odeint(tank,h0,t) # integrate
#y = odeint(tank,h0,t,c, factors) # integrate


# plot results
plt.figure(1)
plt.plot(t,y[:,0],'b-')
plt.plot(t,y[:,1],'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Occupancy')
plt.legend(['ER','ICU'])
plt.show()