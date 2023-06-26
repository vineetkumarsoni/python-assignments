#!/usr/bin/env python
# coding: utf-8

# In[3]:


lst=['1','2','3','4','5']
print(len(lst))


# In[5]:


lst=['1','2','3','4','5']
lst.append('6')# 6 ko as a element rakh dega aur vo bhi sirf last me add hoga 
print(lst)


# In[6]:


lst=['1','2','3','4','5']
lst.insert(3,'2.5')# insert comd me 3 index place ko define krta hai hai that mean vo place jaha element ko insert krana hai 
print(lst)


# In[8]:


lst=['1','2','3','4','5']
lst.remove('3')
print(lst)


# In[10]:


lst1=['1','2','3','4','5']
lst2=['6','7']
lst1.append(lst2)# but isme lst2 as a list add hoga as a element nahi
print(lst1)


# In[11]:


lst1=['1','2','3','4','5']
lst2=['6','7']
lst1.extend(lst2)#lst2 as a elment add hoga isme 
print(lst1)


# In[15]:


#pop and delete
lst=['1','2','3','4','5']
del lst[2] #yaha par 2 index no. hai yaad rakhe 
print(lst)
a=lst.pop(1)# pop se index no.1 ka elem jaa ke 'a' veriable me save hogaya 
print(a)
print(lst)


# In[17]:


lst=['1','2','3','4','5']
lst.remove('3')
print(lst)


# In[18]:


# use of "if"
lst=['1','2','3','4','5']
if '2' in lst:
    print('vineet')


# In[20]:


lst=['1','2','3','4','5']
lst.reverse()
print(lst)


# In[25]:


#sorting me original lst se alag aak lst banayega aur sare oprations usme hi apply honge original wala safe rahenge 
lst=['9','2','6','4','5']
sort_lst=sorted(lst)
print("sorted list:",sort_lst)
print("original list:",lst)


# In[29]:


lst=['9','2','6','4','5']
print("reverse sort list:",sorted(lst,reverse=True))
print("orignal list:",lst)


# In[30]:


# sort func hai isme koi dusri list nahi bnegi original lst me sare oprations honge. 
lst=['9','2','6','4','5']
lst.sort()
print("sorted list:",lst)


# In[32]:


lst=['9','2','6','4','5'] #multi refrence
abc=lst
abc.append('12')
print('original lst:',lst)


# In[42]:


# split func
s="one, two, three, four, five, six, seven, eight, nine, ten"
slst=s.split(',')
print(slst)


# In[40]:


s="mera naam vineet kumar soni hai"
slst=s.split()
print(slst)


# In[45]:


lst=['9','2','6','4','5']
print(lst[1])
print(lst[-3])


# In[47]:


#concept of slicing
n=('one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine', ' ten')
print(n[:])
print(n[0:6])# index no. 0 se 5 tkk sbb print karega 
print(n[::2])#[start:end:step] step means skip kitne index ko karega exmp- agar 2 likha hai mtlb aak elem skip hoga 
print(n[2::])


# In[50]:


#frequency 
f=[1,2,3,2,4,2,4,1,1,5,1,7,5,4,1,2,1,4,5,6,9,8,7,3,6,5,5,7,8,7,8,5,1,5,1,5,1]
print(f.count(1))#1 list me kitni baar repeat ho raha hai 
print(f.count(4))
print(f.count(5))
print(f.count(8))


# In[52]:


#loop in list
n=(' one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine', ' ten')
for ele in n:
    print(ele)


# In[53]:


#without list comprehension 
sq=[]
for i in range(10):
    sq.append(i**3)
print(sq)
    # ye prog 1 se 9 tkk sabhi ke cube dega 


# In[54]:


#with list comprehension 
sq=[]
sq=[i**3 for i in range(10)]
print(sq)


# In[55]:


#comprehension ka use krr ke list2 ko list1 ka double krna hai harr element ko 
list1=[10,20,30,40,50]
list2=[2*i for i in list1]
print(list2)


# In[57]:


lst=[(i,i*10) for i in range(20)]
print(lst)


# In[66]:


# matrix traspose without list comprehension 
matrix = [
    [12,7,3,4],
    [4,5,6,7],
    [7,8,9,10]
]          
transposed=[]
for i in range(4):# ye hai column ke liye 
    lst=[]
    for row in matrix:# ye hai row ke liye 
        lst.append(row[i])
    transposed.append(lst)
        
print(transposed)        


# In[67]:


matrix = [
    [12,7,3,4],
    [4,5,6,7],
    [7,8,9,10]
] 
transposed=[[row[i] for row in matrix] for i in range(4)]
print(transposed)


# In[ ]:




