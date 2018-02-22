
# coding: utf-8

# for loops

# In[1]:

seq = [1,2,3,4,5]


# In[4]:

for num in seq:
    print(num)


# while loop

# In[5]:

i = 1

while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# In[6]:

for x in seq:
    print(x)


# range function

# In[7]:

range(0,5)


# In[8]:

for x in range(0,5):
    print(x)


# In[9]:

list(range(0,5))


# In[10]:

list(range(10))


# List comprehension

# In[11]:

x = [1,2,3,4]


# In[12]:

out = []

for num in x:
    out.append(num**2)


# In[13]:

print(out)


# In[14]:

[num**2 for num in x]


# In[15]:

out = [num**2 for num in x]


# In[16]:

out


# Functions

# In[17]:

def my_func(param1):
    print(param1)


# In[18]:

my_func('hello')


# In[19]:

def my_func2(name):
    print('Hello ' + name)


# In[20]:

my_func2('Jose')


# In[21]:

def my_func3(name='Default name'):
    print('Hello '+name)


# In[22]:

my_func3()


# In[24]:

my_func3('Jose')


# In[25]:

def square(num):
    return num**2


# In[26]:

output = square(2)


# In[27]:

output


# In[28]:

def square2(num):
    """
    This is a docstring
    can go multiple lines
    is a comment
    this func squares a number
    """
    return num**2


# In[29]:

output = square2(2)


# In[30]:

output


# square Shift Tab to see function details

# In[ ]:



