#!/usr/bin/env python
# coding: utf-8

# In[1]:


sh= input("enter hour")
sr= input("enter rate")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("error,enter numeric term only")
    quit()
print(fr,fh)
if fh>40:
    reg= fr*fh
    otp=(fh-40.0)*(fr*0.5)
    print("it is a over time")
    xp=reg+otp
else:
    xp=fh*fr
    print("it is a regular payment")
print("pay",xp)


# In[2]:


#funtions
def call():
    print("hello vineet")
    print("hello ankit")
    print("hello shrey")
call()
print("hello anshu")
call()


# In[6]:


a=('555')
type(a)
b=int(a)
type(b)
c=(b+5)
print(c)


# In[13]:


def greet(coder):
    if coder=='shrey':
        print("pro")
    elif coder=='ankit':
        print("intermidiate")
    else:
        print("faltu admi beroojgaar sala")
greet('ankit')
greet('shrey')
greet('vineet')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




