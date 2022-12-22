# Polynomial plot and Linaer Regression
# Polynomial equation: y = 3x^4 + 2x^3 + x^2 + x

#import numpy as np
import datetime
import matplotlib.pyplot as plt # for plotting
#import scipy.stats as st # linear fit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression

#from sklearn.preprocessing import PolynomialFeatures
#import math

#x = np.array([-2, -1, 0, 1, 2]) # X values for 
#y = np.array([34, 1, 0, 7, 70]) # y values
x = [-2, -1, 0, 1, 2]
y = [34, 1, 0, 7, 70]
#y = np.array([[-2, 34], [-1, 1], [0, 0], [1, 7], [2, 70]])
#z = np.polyfit(x, y, 3)
#x = np.arange(6).reshape(3, 2)

dates=[]
closes=[]
with open("./GM.csv","r") as file:
   file.readline() # exclude first line
   
   for line in file:
       line.strip()
       data=line.split(",")
       dates.append([datetime.datetime.strptime(data[0],"%Y-%m-%d").timestamp()])
       closes.append([float(data[4])])
   file.close()
print(dates[:5])
print(closes[:5])  

plt.plot(dates,closes)
model = make_pipeline(PolynomialFeatures(7), Ridge())
model.fit(dates, closes)
y_plot = model.predict(dates)
plt.plot(dates,y_plot)
plt.show()

