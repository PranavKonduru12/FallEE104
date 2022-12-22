# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("hmeq.csv")

df["Risk"]= "Hello" # Creates new column called "Risk" in csv
                    # Column will be filled with "Hello"

#df.head()

#Converting csv columns to lists
delin = df['DELINQ'].tolist() # Delinquent column as list
risk = df['Risk'].tolist()  #Risk column as list

#print('Delinquent:', delin)

for x in range(len(delin)):     # Read through each element in list
    #print(type(delin[x]))      # length of Delinquent list
    #print(delin[x])
    if delin[x] >= 5:            # DELINQ value greater than 5
        risk[x] = 'HIGH'   # High will be filled in at the same index location
        #print(x, 'High')
        
    elif delin[x] <= 2:          # Logic repats for less than 2
        risk[x] = 'LOW'
        #print(x, 'Low')
    elif delin[x] > 2 and delin[x] < 2:
        risk[x] = 'MEDIUM'
    else:                   #Rest of the Risk list will be filled out with
        risk[x] = 'N/A'  #Medium
    #print(risk[x])
    new_risk = risk # updated list with high, mid will be called new_risk
    
    df["Risk"] = new_risk # updates new risk column in the csv
    

df.to_csv('hmeq_new.csv') #All the changes go to this new csv