#!/usr/bin/env python
# coding: utf-8

# In[13]:


import webbrowser
import time
#webbrowser.open('http://www.google.com')
#def rotina():
#    while(last_time >= '2mins')
starttime = time.time()
#  time.sleep(60.0 - ((time.time() - starttime) % 60.0))
def rotina():
    while True:
        webbrowser.open('http://www.google.com')
        time.sleep(120 - ((time.time() - starttime) % 60))
rotina()


# In[ ]:




