#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=('vineet soni')#single element ko pahchan nahi pata tupple hai ya string
m=('vineet','ankit')
type(n)


# In[4]:


type(m)


# In[5]:


n=('vineet soni',)#single element ko aise likhte hai 
type(n)


# In[7]:


n='vineet soni',
print(type(n))
print(n)


# In[9]:


t=('vineet','mona','sona','tona','dona','pona','lona')
print(t[3])


# In[10]:


print(t[-2])


# In[11]:


#nested tuple
t=('vineet','gona',('sona','tona','dona','pona','lona'))
print(t[2])


# In[13]:


#for print "pona" from nested tuple 
print(t[2][3])


# In[17]:


#slicing
t=('vineet','mona','sona','tona','dona','pona','lona')
print(t[:3])

print(t[:-4])

print(t[::3])


# In[19]:


#immutable tuple 
t=('vineet','mona','sona','tona','dona','pona','lona')
print(t[3])

t[3]="y" #assign nahi hoga kyo ki immutable hai iss liye


# In[24]:


t=('vineet','mona','sona','tona',['dona','pona','lona'])# ye hai tuple ke ander list
#abb hum list ko mutable krr sakte hai
t[4][1]="mutable bcz i am list inside tuple"
print(t)


# In[25]:


#cocat tuple
t=(1,2,3,4)+(5,6,7,8,9)
print(t)


# In[28]:


#repeating func
t=(("vks",)*10)
print(t)


# In[31]:


#delete
t=('vineet','mona','sona','tona','dona','pona','lona')
del t


# In[36]:


t=('vineet','mona','sona','tona','dona','pona','lona')
print('tona'in t)
print('salona' in t)


# In[37]:


t=('vineet','mona','sona','tona','dona','pona','lona')
print(len(t))


# In[38]:


t=('vineet','mona','sona','tona','dona','pona','lona')#"alphbatical order me arreng ho jayega aur data structure bhi change
sot_tuple=sorted(t) # ho jata hai tuple se list ho jata hai 
print(sot_tuple)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




