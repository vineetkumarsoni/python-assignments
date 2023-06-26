#!/usr/bin/env python
# coding: utf-8

# In[1]:


for num in range (1,10):
    print(num)


# In[2]:


for num in range(1,12,2):
    print(num)


# In[9]:


for num in range(10,0,-1):
    print(num)


# In[10]:


int_list =[4,8,-2,10,5]
sum_list=0
for num in int_list:
    sum_list=sum_list+num
print(sum_list)


# In[13]:


# write a program to print the table of 9
num = 9
counter = 1

while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    counter = counter + 1

# What will happen if counter not incremented??
while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    #counter = counter + 1

# 9  *  1  =  9 -> 


# In[16]:


#program  for  table using while loop 
n=int(input())
c=1
while c<=10:
    t=n*c
    print(n,"*",c,"=",t)
    c=c+1# it is a incremental variable kyo ki agar isse nahi lagaoge to table infinite loop
    # me chala jayega aur program crash ho jayega 


# In[2]:


# How to use break statement
int_list = [1,5,7,8,19,13,17,3]

# Find the even value in the given list
for num in int_list:
    print("Current element of the list = ",num)
    if num%2 == 0:
        print("Even number in the list = ",num)
        break

# What is break is removed?
for num in int_list:
    print("Current element of the list = ",num)
    if num%2 == 0:
        print("Even number in the list = ",num)

# How to use continue keyword?
# Print the numbers from for loop and start them from value 1
# but print values on terminal if number is greater than 10

for num in range(1,21): # range(1,21) -> [1,2,3,4,5,6....20]
    if num<10:
        continue
    print(num)


# In[1]:


n=[1,2,4,5,9,8,7,8,5,6,3,2,4,5,7,8,5,6,6,9,8,7,4,4,4,4,5,4,5]
for k in n:
    if k%2==0:
        print("no.is even=",k)


# In[4]:


n=[1,2,4,5,9,8,7,8,5,6,3,2,4,5,7,8,5,6,6,9,8,7,4,4,4,4,5,4,5]
for k in n:
    if k >5:
        print("no. above 5 in list=",k)


# In[7]:


# Declare empty list
L1 = []
#print(type(L1))
print("Initial length of List : ",len(L1))

# Insert values in list
L1.append(5)
L1.append(7)
L1.append(8)
print(L1)



# In[8]:


# How to calculate the length of a list?
len_of_list = len(L1)
print("Lenght of a list : ",len_of_list)


# In[9]:


# how to check is list are equal to each other?
list1 = [1,"Shashank",20,"Hi"]
list2 = [1,"Shashank",20,"Hi"]
print("Lists are equal ?? ", list1 == list2)


# In[10]:


list1 = [1,"Shashank",20,"Hi"]
list2 = [1,"Shashank","Hi",20]
print("Lists are equal ?? ", list1 == list2)


# In[11]:


# List concat
list4 = [1,2,3,4,5]
list5 = [80,90,100,110]
result = list4 + list5
print(result)


# In[ ]:


# how to access list values
list6 = [10,15,20,25,30,35]

# Print all the elements of given list - Option 1
for num in list6:
    print(num)


# In[ ]:


# Print 3rd elements of given list - Option 2
# syntax = list_name[index]
print(list6[0])
print(list6[1])
print(list6[2])
print(list6[3])
print(list6[4])
print(list6[5])


# In[ ]:


# What will happen ??
# Answer will be Index out of range
# print(list6[100])

list7 = [1,"Shashank",1000]
print(list7)

# how to update the value of list index item?
# update Shashank to Rahul
list7[1] = "Rahul"
print(list7)


# In[ ]:


# how to print list elements using length?
for index in range(0, len(list7)): # range(0, 3) -> [0, 1, 2]
    print(list7[index])

list8 = [ 1 , 2 , 50, "Shashank", [6,6,6] , "Rahul"]
print(len(list8)) # What will be the output ???


# Difference between append() and extend()
list9 = [20,30,40]
list10 = ["hi", "hello", "bye"]
list9.append(list10)
print("Output of Append : ",list9)
print("Length after Append : ",len(list9))


# In[ ]:


list11 = [20,30,40]
list12 = ["hi", "hello", "bye"]
list11.extend(list12)
print("Output of Extend : ",list11)
print("Length after Extend : ",len(list11))


# In[ ]:


# List slicing 
list13 = [20,30,40,50,60,80,90]
# Syntax -> list_name[start : end]
# end index is exclusive
print(list13[ 0 : ])
print(list13[ 3 : ])
print(list13[ : ])
print(list13[  : 4 ])
print(list13[ 2 : 6 ])
print(list13[ 0 : : 2]) # 3rd value is for step


# In[ ]:


# How to print the last value of the list?
print(list13[ len(list13) - 1 ])
print(list13[-1]) # negative index -1 means last element of the list

# Print second last element from the list??
print(list13[-2])

# print inout list in reverse direction
print(list13[-1 : : -1])


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




