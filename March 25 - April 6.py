
# coding: utf-8

# In[2]:

print('Hey')


# In[3]:

while True:
    lots of code here
    lots of code here
    lots of code here
    if some_value == True:
        break


# In[4]:

earth_weight = 40
for year in range(1, 16):
    earth_weight = earth_weight + 1
    print ('Year %s = %s' % (year, earth_weight))


# In[5]:

earth_weight = 40
for year in range(1, 16):
    earth_weight = earth_weight + 1
    moon_weight = earth_weight * 0.165
    print ('Year %s = %s' % (year, moon_weight))


# In[6]:

ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
for x in range(1, 6):
    print ('%s %s' % (x, ingredients))


# In[7]:

#Okay, not quite there, haha
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
for x in range (1, 5):
    print ('%s %s' % (x, ingredients[x]))


# In[8]:

#Okay, not quite there, haha
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
for x in range (1, 5):
    print ('%s %s' % (x, ingredients[x]))


# In[9]:

#C'MON
ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']
for x in range (1, 6):
    print ('%s %s' % (x, ingredients [x - 1]))


# In[10]:

x = 0
while x <= 13:
    x = x + 2
    print x


# In[11]:

x = 0
while x <= 13:
    x = x + 2
    x != > 13


# In[12]:

x = 0
while x <= 13:
    x = x + 2
    x !> 13
    print x


# In[13]:

x = 0
while x <= 13:
    x = x + 2
    print x


# In[14]:

list (range(0, 5))


# In[15]:

def testfunc(myname):
    print ('Hello %s' % myname)


# In[16]:

testfunc(Mary)


# In[17]:

def testfunc(myname):
    print ('Hello %s' % myname)
    
testfunc('Mary')


# In[19]:

def testfunc (fname, lname):
    print('Hello %s %s' % (fname, lname))
testfunc('Mary', 'Smith')


# In[20]:

firstname = 'Joe'
lastname = 'Robertson'
testfunc (firstname, lastname)


# In[21]:

def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(10, 10, 5))


# In[ ]:



