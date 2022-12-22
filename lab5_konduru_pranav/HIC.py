#!/usr/bin/env python
# coding: utf-8

# In[2]:


from scipy import integrate
import matplotlib.pyplot as plt


# In[3]:


#wihtout airbag
def no_airbag(t):
    return (16400/((t-68)**2 + 400)) + (1480/((t-93)**2 + 18))


# In[4]:


#with airbag
def airbag(t):
    return 22000/((t-74)**2 + 500) 


# In[8]:


#HIC function
def hic(equ, d, t):
    integration = integrate.quad(equ,t,t+d)
    return (1/1000)*(d*((1/d)*integration[0])**2.5)


# In[9]:


#with airbag
d = 50
x = [v for v in range(0, 160, 1)]
H = [hic(airbag, d, v) for v in x]
print(max(H))


# x = [v for v in range(0, 160, 1)]
# H = [integrate.quad(airbag,v,v+d) for v in x]
# plt.plot(x, H)
# plt.show()
# H = [integrate.quad(without1, v, v+d) for v in t]

# In[30]:


#without airbag
x = [v for v in range(0, 160, 1)]
H_d20 = [hic(no_airbag, 20, v) for v in x]
H_d35 = [hic(no_airbag, 35, v) for v in x]
H_d50 = [hic(no_airbag, 50, v) for v in x]
H_d65 = [hic(no_airbag, 65, v) for v in x]
#plt.plot(x,H_d20, label='d=20')
#plt.plot(x,H_d35, label='d=35')
#plt.plot(x,H_d50, label='d=50')
#plt.plot(x,H_d65, label='d=60')
#plt.xlabel('Time (ms)')
#plt.ylabel('H_d(t)')
#plt.legend()
#plt.show()
print('HIC without when d=20:', round(max(H_d20), 3))
print('HIC without when d=35:', round(max(H_d35), 3))
print('HIC without when d=50:', round(max(H_d50), 3))
print('HIC without when d=65:', round(max(H_d65), 3))


# In[29]:


#with airbag
x = [v for v in range(0, 160, 1)]
H_d20 = [hic(airbag, 20, v) for v in x]
H_d35 = [hic(airbag, 35, v) for v in x]
H_d50 = [hic(airbag, 50, v) for v in x]
H_d65 = [hic(airbag, 65, v) for v in x]
plt.plot(x,H_d20, label='d=20')
plt.plot(x,H_d35, label='d=35')
plt.plot(x,H_d50, label='d=50')
plt.plot(x,H_d65, label='d=60')
plt.xlabel('Time (ms)')
plt.ylabel('H_d(t)')
plt.legend()
plt.show()
print('HIC with airbag when d=20:', round(max(H_d20), 3))
print('HIC with airbag when d=35:', round(max(H_d35), 3))
print('HIC with airbag when d=50:', round(max(H_d50), 3))
print('HIC with airbag when d=65:', round(max(H_d65), 3))


# In[ ]:




