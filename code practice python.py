#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")


# In[ ]:





# In[2]:


#IF ELSE  ELIF 
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")


# In[6]:


#FOR LOOP
N="VINEET KUMAR SONI"
for  k  in N:
    print (k, end =",")
    if (k=="M"):
        print ("this name have consonent")


# In[3]:


name = "Harry"
friend = "Rohan"
anotherFriend = 'Lovish'
apple = '''He said, 
Hi Harry
hey I am good
"I want to eat an apple'''
 
print("Hello, " + name)
# print(apple) 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)


# In[1]:


name ="vineetsoni"
for v in name :
    print(v)


# In[2]:


name ="vineetsoni"
for v in name :
    print(v)
    if (v =="e"):
        print("this is special")


# In[3]:


for k in range(1, 12, 3):
  print(k)


# In[2]:


i=0
while (i<=10):
    print(i)
    i=i+1
print("done with loop")


# In[7]:


count=10
while(count >0):
    print(count)
    count=count-1


# In[11]:


i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")


# In[14]:


for i in range (15):
    print("5 X",i,"=",5*i)
    if (i==12):
        break


# In[16]:


# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")


# In[1]:


def avg(a,b,c):
    print("average of no. is",(a+b+c)/2 )
    
avg(12,2,12)


# In[ ]:


marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)


# In[20]:


marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
if 5 in marks :
    print("yess")
else :
    print("no")


# In[21]:


marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
if "5"in marks :#brcause 5 as a integer  hai  list me not as string
    print("yess")
else :
    print("no")


# In[22]:


marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
print(len(marks))


# In[1]:


lst=[i*i for i in range (10)]
print(lst)


# In[3]:


lst=[i*i for i in range (10) if i%2==0]
print(lst)


# In[ ]:


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
m = [900, 1000, 1100]
k = l + m
# print(k)
# l.extend(m)
print(l)


# In[5]:


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
print(l.count(1))


# In[8]:


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.insert(1,786)
print(l)


# In[ ]:


tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)


# In[16]:


tup = (1, 2, 76, 342, 32, "green", True)
c=len(tup)
print(c)


# In[18]:


tup = (1, 2, 76, 342, 32, "green", True)
print(tup[c-1])#neg indeex to postive conversion 


# In[21]:


tup2 = tup[1:4]
print(tup2)


# In[ ]:


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)


# In[24]:


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res=tuple1.index(3,2,9)#first me vo likho jis no. ka count chahiye uske baad slicing likho kaha se kaha tkk
print('Count of 3 in tuple1 is:', res)


# In[25]:


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
print(type(tuple1))


# In[27]:


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
tl=list(tuple1)
print(tl)
print(type(tl))


# In[31]:


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
print(type(countries))


# In[32]:


import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime


# In[33]:


import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!")


# In[ ]:


letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))


# In[3]:


l= "myname is {} and i am from {}"
n=input(' ')
p=input(' ')
print(l.format(n,p))


# In[6]:


print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}"))


# In[9]:


country = "India"
name = "Harry"


print(f"Hey my name is {name} and I am from {country}")


# In[1]:


# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(92))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)


# In[2]:


def febonachi(f(n)):
  if (n == 0) :
    return 0
    elif(n == 1):
        return 1
  else:
    return f(n-1) + f(n-2)


print(fabonachi(5))


# In[1]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)


# In[2]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)


# In[3]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)


# In[4]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)


# In[5]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)


# In[6]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))


# In[7]:


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities2.difference(cities))


# In[8]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))


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





# In[ ]:





# In[ ]:





# In[ ]:




