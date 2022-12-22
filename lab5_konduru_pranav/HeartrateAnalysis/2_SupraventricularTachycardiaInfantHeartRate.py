#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Supraventricular tachycardia infant heart rate
#import packages
#import packages
get_ipython().system('pip install heartpy')

import heartpy as hp
import matplotlib.pyplot as plt

sample_rate = 250


# In[14]:


#data = hp.get_data('1_Output_mono.csv')
#data = hp.get_data('data.csv')
data = hp.get_data('heartbeat_d_Output_mono_normalized.csv')

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()


# In[15]:


#run analysis
wd, m = hp.process(data, sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))


# In[ ]:





# In[ ]:





# In[ ]:




