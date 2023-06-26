#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#def fuction-name(parameter):
#string to explain about function
#statement(s)


# In[ ]:


#working of funcion
def functionname: ("colan is very imp")
 



functionname():(func @ call)
    
    


# In[5]:


def naam_likh(name):
    """
    naam likh ke dunga jiska bolega uska #ye sirf statement hai jo run nahi hota sirf batata hai fuction kaam kya krta hai
    """
    print("Hello " + str(name))
naam_likh("Next")#calling of the function    


# In[7]:


#to print doc string of afunction
print(naam_likh.__doc__) #doo baar"__" underscore laga hai yaad se  


# In[25]:


#define a function jo list ko add krta ho
def sum_karo(lst):
    """
    ye function list k asum dega
    """
    sum=0
    for num in lst:#jo list hai usko aak dabba asign hoga usi naam "sum hai"
        #aur jo list ke ander number hai uska naam "num" hai jo 
        sum = sum + num
    return sum# sum me store kranr ka liye


# In[26]:


s = sum_karo([1,2,3,4,5,6,7,8,9,10])
print(s)


# In[29]:


global_var = "tera bhai world famous hai"
def test_life_time():
    """
    check krrke batat hu 
    """
    local_var ="mai local var hu"
    print(local_var)
    print(global_var)


# In[30]:


#calling of function
test_life_time()
print(global_var)


# In[31]:


# but local variable function ke  bahar define nahi hoga iss liye error dega 
print(local_var)


# In[36]:


# gcd ya hcf kaise nikale
def hcf_nikalega_apun(a,b):
    """
    tera bhai hcf nikal ke dega 
    """
    smaller = b if a > b else a
    
    hcf = 1# ye uss condition ke liye define kiya gaya hai jisme apko koi hcf nahi milraha hai 
    for i in range(1, smaller+1):
        if(a%i ==0) and (b%i ==0):# use of and operater
            hcf = i# agar i a aur b dono fully divide kr deta hai to vo 'i' ki value hi hcf ke barabar hogi 
    return hcf
num1=15
num2=30

print("hcf of {0}and {1} is {2}".format(num1,num2,hcf_nikalega_apun(num1,num2,)))


# In[ ]:


#PYTHONS BUILT IN FUNCTION 


# In[37]:


num=-100
print(abs(num))#absolute function 


# In[40]:


# check the right type function
lst=[1,2,3,4,5,6,7,8,9]
print(all(lst))# ye funtion check karega null aur false value ko


# In[46]:


lst=[1,2,'vineet',4,5,6,7,8,9]
print(all(lst))


# In[47]:


lst=[1,2,'vineet',4,0,5,6,7,8,9]
print(all(lst))#zero ke karan null ho gaya that why false return karega 


# In[48]:


#to get the all function of list
lst=[1,2,'vineet',4,0,5,6,7,8,9]
print(dir(lst))


# In[49]:


# to get the quotient and remender
print(divmod(7,2))     # it is 7 divided by 2
#output me 3 quotient hai aur 1 remender hai  in tuple format


# In[51]:


#print index and respective value 
lst=[1,2,'vineet',4,0,5,6,7,8,9]
for index,num in enumerate(lst):#enumerate main function hai
    print("index {0} has value {1}".format(index,num))


# In[54]:


lst=[1,2,'vineet',4,0,5,6,7,8,9]
for index,num in enumerate(lst,8):#enumerate main function hai # 8 dalne se indexing ki starting 8 se hogi
    print("index {0} has value {1}".format(index,num))


# In[61]:


#filter function bahut use hota ahai data science me achhe sikhe 
# ise do chise chahiye pahli 'function ka naam' dusra "list"
def postive_numb_dunga_mai(num):
    """mai postive no hi dunga lst se nikal ke"""
    if num >0:
        return num


# In[63]:


num_lst=range(-30,20)#range creat karega
print(list(num_lst))#given range ko lst me convert karne ke liye 
postv_no_lst=list(filter(postive_numb_dunga_mai,num_lst))# filter do chis mangega 1)funct name 2)list
print(postv_no_lst)


# In[64]:


#same program for negative output from list
def negative_numb_dunga_mai(num):
    """mai negative  no hi dunga lst se nikal ke"""
    if num <0:
        return num


# In[65]:


num_lst=range(-30,20)#range creat karega
print(list(num_lst))#given range ko lst me convert karne ke liye 
negative_no_lst=list(filter(negative_numb_dunga_mai,num_lst))# filter do chis mangega 1)funct name 2)list
print(negative_no_lst)


# In[66]:


#isinstance function
lst=[1,2,3,4,5,6,7,8,9,10]
print(isinstance(lst,list))# kya lst sachme list hai agar haa to true nahi to false 
lst1=(1,2,3,4,5,6,7,8,9,10)
print(isinstance(lst1,list) )


# In[67]:


#without map function 
lst=[1,2,3,4,5,6,7,8,9,10]
square=[]
for num in lst:
    square.append(num**2)#square list ke ander number in lst ka square krr ke rakhte jaoo
print(square)


# In[69]:


#with map function 
def power_karega_bhai(num):
    return num**2

square=list(map(power_karega_bhai,lst))# do chise mangega 1) funct ka naam ,2) list
print(square)


# In[70]:


#reduce function
#did rolling computation 
lst=[1,2,3,4,5,6,7,8,9,10]
from functools import reduce 
def multiply(x,y):
    return x*y;
product = reduce(multiply,lst)
print(product)


# In[5]:


#function argument 
# function call,name,msgdef greet(name,msg)
def greet(name,msg):
    """
    ye funtion greeting karta hai sabko
    """
    print("my name is {0},{1}".format(name,msg))
greet("vineet kumar soni","the pro coder")


# In[6]:


# but given error when you give only one argument
greet("vineet kumar soni")#function ko chalne ke liye do argument chahiye hi chahiye 


# In[10]:


# single argument ki problem ko solve krne ke liye aya hai "default argument"
def greet(name,msg="is pro coder"):# but most imp baat default wala argument hamesha 2nd position me hi define kare 
    """
    ye funtion greeting karta hai sabko
    """
    print("my name is {0},{1}".format(name,msg))


# In[11]:


greet("vineet kumar soni")# second argument "msg" by default aa gaya 


# In[19]:


#arbitrary no. of fuctions
def greet(*names):
    """
   jitne chahe naam daldo sbb ko greet karega mai
   """
    print(names)
    for name in names:
        print("hello,","{0}".format(name))
greet("vinnet soni","ankit soni","shrey soni","ekta soni")


# In[ ]:


#RECURSIVE FUNCTION 
# WHEN FUNCTION CALL ITSELF with "reduce parameter" 
#DISADVANTAGE= MEMORY LETA HAI
#ADVANTAGE = CODE YA FUCNTION KO REUSE KRR SAKTE HAI
# code look and feel good and clean
# easy to sequence genration


# In[2]:


#recursive function 
# to find factorial
def factorial(num):
    """
    recursive
    """
    return 1 if num==1 else (num * factorial(num-1))
num=10
print("factorial of{0}is{1}".format(num,factorial(num)))


# In[ ]:


#lambda function 
#it is define without a name 

#lamda arguments:expression


# In[3]:


#without lambda 
def double(x):
    return x*2
print(double(10))


# In[5]:


#with lambda 
double= lambda x: x*2  #structure =function name = lambda func :expression
print(double(5))


# In[8]:


# lambda function with map
lst=[1,2,3,4,5,6,7,8,9]
new_lst=list(map(lambda x:x*5,lst)) #for multiple of 5
print(new_lst)


# In[9]:


# same prog for power of 5
lst=[1,2,3,4,5,6,7,8,9]
new_lst=list(map(lambda x:x**5,lst)) #for pow of 5
print(new_lst)


# In[12]:


# use lambda with filter 
lst=[1,2,3,4,5,6,7,8,9]
even_lst=list(filter(lambda x:(x%2 ==0),lst))
print(even_lst)


# In[13]:


# lambda in reduce function
from functools import reduce 
lst=[1,2,3,4,5,6,7]
product_lst= reduce(lambda x,y:x*y,lst)
print(product_lst)


# In[ ]:




