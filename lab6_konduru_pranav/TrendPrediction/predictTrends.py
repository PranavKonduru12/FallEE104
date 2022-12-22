#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

# To get data for only three months starting from first date
three_months = datetime.datetime(2020, 7, 31)

#Read CSV file of COVID cases from May to October 2020
df = pd.read_csv("SixMonths_COVID-19_case_counts_by_date.csv", parse_dates = ['Date'])

#df["Three Months"] = df["Date"]
#date = pd.to_datetime(df["Date"])
#print(date)

#df = df[ (df['Three Months'] <= three_months) ] 

#df = df[ (df['Three Months'] <= three_months) ] # For the three months

#total_cases = df['Total_cases'].tolist() # total cases converted to list
#print(total_cases)

#new_cases = df["New_cases"].tolist()  # nuew cases converted to list
#print(new_cases)

#trend prediction
#list_three_months = df['Total_ThreeM'].tolist() # converted to list
#total_cases = df['Total_cases'].tolist()
x_values = np.arange(df['Last_four_months'].size) # Counts each date as one element
#print(x_values)

z = np.polyfit(x_values, df['Total_cases'], 2)
#print(z)
fit_function = np.poly1d(z)
df['Predict Total Cases'] = fit_function(x_values)
#print(df['Predict Total Cases'])
#print(fit_function(x_values))
#print(fit_function)

#df.plot(x='Date',y='Total_cases') 
df.plot(x='Three_months', y='Total_ThreeM')
#plt.plot(df['Three_months'], fit_function(x_values)) 
#df.plot(x='Date',y='Total_cases')
plt.xlabel('Dates')
plt.ylabel('Cases')
plt.title('Three Months Covid19 Totals cases', color='black')
plt.tight_layout()

df.plot(x='Last_four_months', y='Predict Total Cases')
#plt.plot(df['Three_months'], fit_function(x_values)) 
#df.plot(x='Date',y='Total_cases')
plt.xlabel('Dates')
plt.ylabel('Cases')
plt.title('Polyfit Covid19 Totals cases', color='black')
#plt.tight_layout()
#plt.show()