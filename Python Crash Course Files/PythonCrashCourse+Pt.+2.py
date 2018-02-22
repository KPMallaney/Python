
# coding: utf-8

# Dictionary

# In[2]:

d = {'key1':'value','key2':123}


# In[3]:

d['key1']


# In[4]:

d['key2']


# In[5]:

d = {'k1':[1,2,3]}


# In[6]:

d


# In[7]:

d['k1']


# In[8]:

d['k1'][1]


# In[9]:

my_list = d['k1']


# In[10]:

my_list[0]


# In[11]:

d = {'k1':{'innerkey':[1,2,3]}}


# In[12]:

d['k1']


# In[13]:

d['k1']['innerkey']


# Boolean

# In[14]:

True


# In[15]:

False


# Tuples and Sets

# In[16]:

my_list = [1,2,3]


# In[17]:

my_list[0]


# In[18]:

t = (1,2,3)


# In[19]:

t[0]


# In[20]:

my_list


# In[21]:

my_list[0]


# In[22]:

my_list[0] = 'NEW'


# In[23]:

my_list


# In[24]:

t[0] = 'NEW'


# Tuples do not support item assignment

# Sets

# In[25]:

{1,2,3}


# In[26]:

{1,1,1,2,3,4,4}


# Only unique elements

# In[27]:

set([1,1,1,11,2,2,2,2,5,5,5,5])


# In[28]:

s = {1,2,3}


# In[29]:

s.add(5)


# In[30]:

s


# In[31]:

s.add(5)


# In[32]:

s


# Comparison operators

# In[33]:

1 > 2


# In[34]:

1 < 2


# In[35]:

1 >= 2


# In[36]:

1 <= 1


# In[37]:

1 == 1


# In[38]:

1 == 2


# In[39]:

1 != 3


# In[40]:

'hi' == 'bye'


# In[41]:

1 < 2


# In[42]:

1 < 2 and 2 < 3


# In[43]:

(1 < 2) and (2 > 3)


# In[44]:

(1 < 2) or (2 > 3)


# In[ ]:




# In[45]:

if 1 < 2:
    print('yes')


# In[46]:

if True:
    print('perfrom code')


# In[ ]:




# In[47]:

if 1 == 2:
    print('First')
else:
    print('last')


# In[ ]:




# In[48]:

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('last')


# In[ ]:



