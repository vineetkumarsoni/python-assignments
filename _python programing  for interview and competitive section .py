#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


#to find prime no.


# In[3]:


from math import *
def fun(n):
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False 
    for i in range(5,int(sqrt(n))+1):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
t= int(input())
while t:
    n=int(input())
    print(fun(n))
    t= t-1


# In[ ]:


x =int(input('no.dalo bye'))
if(x %2 ==0):
    print("this is a even")
else:
    print("this is odd")


# In[ ]:


x = int(input("put the year"))
if(x % 400 == 0):
    print("year is leap year")
elif(x % 4==0 and x % 100!=0):
    print("this is leap year")
else:
    print("year is not leap"
    


# In[4]:


#leap year
x = int(input())
if x%400==0:
    print("year is leap")
elif(x% 4 ==0 and x%100!=0):
    print("leap hai ")
else:
    print("non leap")
    


# In[5]:


#how to remove duplicate from list
no=[]
n= int(input())
for i in range (n):
    no.append(input())
s= set(no)
no=list(s)
print(s)
 
    


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


a= "jkjh"
print(a)

