#!/usr/bin/env python
# coding: utf-8

# In[2]:


# sequence of unicode character 
#it is a character arrey
# support indexing
mys="hello brother this vineet kumar soni"
print(mys[10])
print(mys[-10])
print(mys[3:16])


# In[38]:


#change string into a list class 
s1='vineet'
print(type(s1))
s2=list(s1)
print(type(s2))


# In[3]:


myst='vineet'
myst[4]='soni'# immutable in nature


# In[15]:


s1=' vineet '
s2='kumar '
s3='soni'
print(s1+s2+s3)
s=s1 + s2 + s3
print(s*4)


# In[17]:


#count by for loop
count =0
for l in 'hello vineet':
    if l=="e":
        count +=1
print(count,'baar aya hai')        


# In[20]:


print("v" in "hello vineet")
print('k'in 'hello vineet')


# In[26]:


# functions in program
'VINEET'.lower()


# In[25]:


'vineet'.upper()


# In[27]:


"mera naam vineet kumar soni hai".split()# change in list 


# In[30]:


'-'.join(['mera', 'naam', 'vineet', 'kumar', 'soni', 'hai'])


# In[33]:


"mera naam vineet kumar soni hai".find('ee')


# In[34]:


"vineet kumar soni".replace("soni","saraf")


# In[35]:


s1="vineet kumar soni"
s2=s1.replace("soni",'saraf')
print(s1)
print(s2)


# In[42]:


#python program to check pallindrome ,vo words jo sidha padho ya ulta same hi rahta hai jaise "madam",malalam
s1='NITin'
s1= s1.lower()# phale sabhi alphabet ko lower ya uppercase me karenge
rev_s1=reversed(s1)
if list(s1) ==  list(rev_s1):
    print("pallindrom Hai ye")
else:
    print("pallindrom nahi hai")


# In[52]:


s1="mera naam vineet kumar soni hai"
s2=s1.split()
s2.sort()# yahi sabhi split words ko alphabaticaaly arenge karega 
for word in s2:#vertically print karne ke liye 
   print(word)#alphabatical order me arrenge ho jayega 

