
# coding: utf-8

# In[1]:

def times2(var):
    return var*2


# In[3]:

times2(5)


# Map function

# In[4]:

seq = [1,2,3,4,5]


# In[6]:

map(times2,seq)


# In[7]:

list(map(times2,seq))


# Lambda expression

# In[8]:

lambda var:var*2


# In[9]:

t = lambda var:var*2


# In[10]:

t(6)


# In[11]:

list(map(lambda num: num*3,seq))


# filter function

# In[12]:

filter(lambda num: num%2==0,seq)


# In[13]:

list(filter(lambda num: num%2 == 0,seq))


# Methods

# In[14]:

s = 'hello my name is Sam'


# s. tab to view all methods

# In[15]:

s.lower()


# In[16]:

s.upper()


# In[17]:

s.split()


# In[18]:

tweet = "Go sports! #sports"


# In[19]:

tweet.split()


# In[20]:

tweet.split('#')


# In[21]:

tweet.split('#')[1]


# In[22]:

d = {'k1':1,'k2':2}


# In[23]:

d


# In[24]:

d.keys()


# In[25]:

d.items()


# In[26]:

d.values()


# In[27]:

lst = [1,2,3]


# In[28]:

lst.pop()


# In[29]:

lst


# In[30]:

lst = [1,2,3,4,5]


# In[31]:

item = lst.pop()


# In[32]:

lst


# In[33]:

item


# In[34]:

first = lst.pop(0)


# In[35]:

lst


# In[37]:

first


# In[38]:

lst.append('new')


# In[39]:

lst


# in operator

# In[40]:

'x' in [1,2,3]


# In[41]:

'x' in ['x','u','y']


# tuple unpacking

# In[42]:

x = [(1,2),(3,4),(5,6)]


# In[43]:

x


# In[44]:

x[0]


# In[45]:

x[0][1]


# In[46]:

for item in x:
    print(item)


# In[47]:

for (a,b) in x:
    print(a)


# In[48]:

for(a,b) in x:
    print(b)


# In[49]:

for a,b in x:
    print(b)


# In[50]:

for a,b in x:
    print(a)
    print(b)


# In[ ]:



