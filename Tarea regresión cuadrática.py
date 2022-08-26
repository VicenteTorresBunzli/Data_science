#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import scipy.stats as stats

#Datos de felicidad segun tiempo de juego en LoL del 1 al 100
horas = [6, 9, 12, 12, 15, 21, 24, 24, 27, 30, 36, 39, 45, 48, 57, 60]
felicidad = [12, 18, 30, 42, 48, 78, 90, 96, 96, 90, 84, 78, 66, 54, 36, 24]


# In[13]:


import matplotlib.pyplot as plt

#crear grafico de puntos
plt.scatter(horas, felicidad)


# In[14]:


import numpy as np

#regresion con exponente 2
model = np.poly1d(np.polyfit(hours, happ, 2))

#Añadir variables al grafico
polyline = np.linspace(1, 60, 50)
plt.scatter(horas, felicidad)
plt.plot(polyline, model(polyline))
plt.show()


# In[15]:


print(model)


# In[ ]:




