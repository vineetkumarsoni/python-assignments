#!/usr/bin/env python
# coding: utf-8

# In[6]:


# it is unordered collection of items
# index not supported like as set 
my_dict={}
print(my_dict)#empty
my_dict=()# empty
print(my_dict)


# In[3]:


md={1:"vineet",2:"ankit"}
print(md)


# In[4]:


md={1:"vineet",2:"ankit",3:['1997','1994']}#mixed keys 
print(md)


# In[8]:


# dictionary with list of tuple 
md=dict([(1,'vineet'),(2,'ankit')])
print(md)
print(type(md))


# In[9]:


# access of dictionary
md={'name':'vineet','year':'1997'}
print(md['year'])


# In[10]:


print(md['age'])# show key error mean ki aisi koi key available nahi hai dict ke ander 


# In[12]:


#other way to access the dict
print(md.get('name'))# get method
# iss methode ka sabe bada fayeda
print(md.get('age'))
#ye methode unavailable key in dictionary ke liye kabhi bhi error  nahi fekegi sirf 'none' show karegi 


# In[16]:


# update the dict
md={'name':'vineet','year':'1997'}
md['name']='vinnu'
print(md['name'])
print(md)


# In[17]:


#add new key
md['Degree']='B.E(e.e.e)'
print(md)


# In[19]:


#remove a perticular item from dictionary
md={'name': 'vinnu', 'year': '1997', 'Degree': 'B.E(e.e.e)'}
print(md.pop('year'))
print(md)


# In[21]:


md={'name': 'vinnu', 'year': '1997', 'Degree': 'B.E(e.e.e)'}#remove any random key
md.popitem()
print(md)


# In[22]:


#delete
md={'name': 'vinnu', 'year': '1997', 'Degree': 'B.E(e.e.e)'}
del md['name']
print(md)


# In[23]:


#delete all items in a list 
md.clear()
print(md)


# In[25]:


#DICTIONARY METHODS # copy function  to copy of given dictionary
md={'name': 'vinnu', 'year': '1997', 'Degree': 'B.E(e.e.e)'}
md1=md.copy()
print(md1)


# In[27]:


# "fromkeys" function assign same value for different keys 
subj={}.fromkeys (['math','english','hindi', 'socal', 'sansakrit','bio'],0)
print(subj)


# In[28]:


#to view the all items of dictionary in a list of tuple formate
subj={'math':'english','hindi':'socal','sansakrit':'bio'}
print(subj.items())


# In[29]:


#to show only the keys of dictionary 
subj={'math':'english','hindi':'socal','sansakrit':'bio'}
print(subj.keys())


# In[31]:


#to show only the vaules of dictionary 
subj={'math':'english','hindi':'socal','sansakrit':'bio'}
print(subj.values())


# In[32]:


# TO GET KNOW ABOUT THE ALL FUNCTIONS OF DICTIONARY 
d={}
print(dir(d))


# In[34]:


#TO PRINT THE PAIR OF DICTIONARY by unsing for loop
subj={'math':'english','hindi':'socal','sansakrit':'bio'}
for pair in subj.items():
    print(pair)


# In[39]:


#PRINT DICTIONARY ITEMS THOSE FOLLOW CERTAIN CONDITIONS BY USING "IF"
# max use  hota iska data extraction me 
d={'a':1,'b':2,'c':3,'d':4,'e':5}
new_d={k:v for k,v in d.items() if v >= 3}
print(new_d)# keval wahi print honge jisme value 3 ya 3 se bada hai 


# In[40]:


# iss me data ko manuputlate kiya gaya hai 
#jaise sabhi keys ke sath 'c'add ho jayega aur sabhi value double ho jayegi jo 3 ya 3 badi hai 
d={'a':1,'b':2,'c':3,'d':4,'e':5}
new_d={k+'c':v*2 for k,v in d.items() if v >= 3}
print(new_d)


# In[ ]:





# In[ ]:




