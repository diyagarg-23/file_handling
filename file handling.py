#!/usr/bin/env python
# coding: utf-8

# # FILE HANDLING

# In[4]:


f = open('My India.txt','r')
for each in f:
    print(each) #this will 


# In[8]:


f = open('My India.txt','r')
print(f.read())


# In[9]:


#python code to illustrate with()
with open('My India.txt') as f:
    data = f.read()
    print(data)


# In[10]:


#python code to illustrate read() mode character wise
file = open('My India.txt','r')
print(file.read(10))


# # #  Working in Write mode

# In[11]:


file = open('Mumbai.txt','w')
file.write('This is the write command')
file.write('It allows us to write in a particular file')
file.close()


# In[12]:


with open('file.txt','w') as f:
    f.write('hello world')


# In[13]:


#python code to illustrate append() mode
f2 = open('Mumbai.txt','a')
f2.write('this will add this line')
f2.close()


# In[14]:


try:
    with open('filename.txt','r') as file:
        data = file.read()
        print('user data read successfully: ')
        print(data)
except FileNotFoundError:
    print('please check the file path')


# In[15]:


#error
amount = 10000
if (amount >2999):
    print('you are eligible to purchase course')


# In[16]:


#exception
marks = 10000
a= marks/0
print(a)


# In[17]:


#type error
x = 5
y = 'hello'
z = x+y


# In[2]:


#finally keyword in python
#python provides a keyword finally,which is always executed after the try and except blocks.
#The final block always executes after the normal termination of teh try block or after the
#try block terminates due to some exception.

try:
    k = 5//0
    print(k)
    
except ZeroDivisionError:
    print("can't divide by zero")
    
finally:
    print('this is always executed')
    
#the code attempts to perform integer division by zero,resulting in a ZeroDivisionError.
#it catches the exception and prints 'can't divide by zero'
#regardless of the exception,the finally block is executed and prints 'this is always executed.'


# In[ ]:




