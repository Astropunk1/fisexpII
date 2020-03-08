#!/usr/bin/env python
# coding: utf-8

# In[89]:


#HISTOGRAMA PERIODO PENDULO, FISICA EXP II
import pandas as pd
import numpy as np
from matplotlib.pylab import *

data=pd.read_excel('medidas.xlsx', skiprows=0)
i=1
an=[]

def per():  #Creamos una funcion que halla los periodos como la sucesion recursiva An = (T1+4k - T4k)/2 + T4k - (An-1)
    for i in range(1,11):
        if i==1:
            an.append(((((data.iloc[1+4*i,])-(data.iloc[4*i,]))/2)+(data.iloc[4*i,])))
        else:
            an.append(((((data.iloc[1+4*i,])-(data.iloc[4*i,]))/2)+(data.iloc[4*i,]))-((((data.iloc[1+4*(i-1),])-(data.iloc[4*(i-1),]))/2)+(data.iloc[4*(i-1),])))            
    return an
df=per() #hacemos una lista con los periodos

plt.figure(figsize=(10,10))
plt.hist(df[1:] , bins=5) #graficamos el histograma omitiendo la primera fila de datos
plt.title("Histograma periodo",fontsize=30) ; plt.xlabel("Periodo (µs)",fontsize=20) ; plt.ylabel("Repeticiones",fontsize=20) 
plt.axvline(x=np.mean(df[1:])-np.std(df[1:]), ls = "--", color='#2ca02c', alpha=0.7) #desviacion estandar
plt.axvline(x=np.mean(df[1:])+np.std(df[1:]), ls = "--", color='#2ca02c', alpha=0.7)
print(pd.DataFrameFrame(df))
print("Media de los periodos= %s µs" % (np.mean(df[1:])))
print("Desviacion estandar = %s µs" % (np.std(df[1:])))



# # 

# In[ ]:




