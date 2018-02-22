
# coding: utf-8

# Basic numbers and arithmatic

# In[1]:

1


# In[2]:

1.0


# Addition

# In[3]:

1+1


# Multiplication

# In[5]:

1*3


# Division

# In[6]:

1 / 2


# Exponents

# In[7]:

2 ** 4


# Order of operations

# In[8]:

2 + 3 * 5 + 5


# In[9]:

(2+3) * (5+5)


# Modulo

# In[10]:

4 % 2


# In[11]:

5 % 2


# In[12]:

8 % 2


# Variable assignments

# In[13]:

var = 2


# In[14]:

var


# In[15]:

x = 2
y = 3


# In[16]:

x + y


# In[17]:

x = x+x


# In[18]:

x


# In[19]:

x = x+x


# In[20]:

x


# In[21]:

x


# In[24]:

name_of_var = 12


# Strings

# In[25]:

'single quote'


# In[26]:

"this is a string"


# In[27]:

"I can't go"


# In[28]:

x = "hello"


# In[29]:

x


# In[30]:

print(x)


# In[31]:

num = 12
name = 'Sam'


# Format Strings

# In[33]:

print('My number is {} and my name is {}'.format(num,name))


# In[34]:

print('My number is {one} and my name is {two}'.format(one=num,two=name))


# Indexing strings

# In[35]:

s = 'hello'


# In[36]:

s[0]


# In[37]:

print(s[0])


# In[38]:

s[4]


# Slicing

# In[39]:

s = 'abcdefghijk'


# In[40]:

s[0]


# In[41]:

s[0:]


# In[42]:

s[:3]


# In[43]:

s[3:6]


# Lists

# In[44]:

[1,2,3]


# In[45]:

['a','b','c']


# In[46]:

my_list = ['a','b','c']


# In[47]:

my_list.append('d')


# In[48]:

my_list


# In[49]:

my_list[0]


# In[50]:

my_list[1:3]


# In[51]:

my_list[0] = 'NEW'


# In[52]:

my_list


# In[53]:

nest = [1,2,[3,4]]


# In[54]:

nest


# In[55]:

nest[2]


# In[56]:

nest[2][1]


# In[58]:

nest = [1,2,3,[4,5,['target']]]


# In[59]:

nest[3]


# In[60]:

nest[3][2]


# In[61]:

print(nest[3][2][0])


# In[ ]:



