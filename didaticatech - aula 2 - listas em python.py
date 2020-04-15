#!/usr/bin/env python
# coding: utf-8

# In[22]:


lista1 = [1,2,3]
type(lista1)


# In[3]:


lista2 = [[1,2,3],[4,5,6],[7,8,9]]


# In[4]:


type(lista2)


# In[16]:


select = lista2[1]
print(select)
type(select)


# In[19]:


select = lista2[0][1]
print(select)
type(select)


# In[28]:


#--------------------------------#
import random
cidades = ['rio','sp','bh','pa']
escolhida = random.choice(cidades)
print('A cidade é escolhida:',escolhida)


# In[42]:


a = [1,2,3]
a.append(15)
print(a)


# In[43]:


b = [7,8,9]
for i in b:
    a.append(i)
print(a)


# In[ ]:




