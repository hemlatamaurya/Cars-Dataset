#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[2]:


import pandas as pd

car = pd.read_csv(r"C:\Users\Admin\Downloads\file.csv")
car.head()


# In[3]:


car.shape


# In[ ]:


# Data Cleaning
# find all the null value in the dataset if there is any null value on any column then fill it with the mean of that column


# In[51]:


import pandas as pd
car = pd.read_csv(r"C:\Users\Admin\Downloads\file.csv")

car.isnull()        # is used to check the null value present in column
                    # False showing null value is not present and true showing null value is present
    
car.isnull().sum()


# In[23]:


import pandas as pd
car = pd.read_csv(r"C:\Users\Admin\Downloads\file.csv")
car.isnull().sum()
car
car['Make'].fillna(car['Make'].mode()[0])

car['Make'].fillna(car['Make'].mode()[0], inplace=True)
car.isnull().sum()


# In[50]:


car.isnull().sum()

car['Cylinders'].fillna(car['Cylinders'].mode()[0], inplace=True)
car.isnull().sum()

car['Model'].fillna(car['Model'].mode()[0], inplace=True)
car.isnull().sum()

car['Type'].fillna(car['Type'].mode()[0],inplace=True)
car.isnull().sum()

car['Origin'].fillna(car['Origin'].mode()[0], inplace=True)
car.isnull().sum()

car['DriveTrain'].fillna(car['DriveTrain'].mode()[0], inplace=True)
car.isnull().sum()

car['MSRP'].fillna(car['MSRP'].mode()[0], inplace=True)
car.isnull().sum()

car['Invoice'].fillna(car['Invoice'].mode()[0], inplace=True)
car.isnull().sum()


car['EngineSize'].fillna(car['EngineSize'].mode()[0], inplace=True)
car.isnull().sum()

car['Horsepower'].fillna(car['Horsepower'].mode()[0], inplace=True)
car.isnull().sum()

car['MPG_City'].fillna(car['MPG_City'].mode()[0], inplace=True)
car.isnull().sum()

car['Weight'].fillna(car['Weight'].mode()[0], inplace=True)
car.isnull().sum()

car['Wheelbase'].fillna(car['Wheelbase'].mode()[0], inplace=True)
car.isnull().sum()

car['Length'].fillna(car['Length'].mode()[0], inplace=True)
car.isnull().sum()



# In[ ]:


# Value count Function
# Chaeck what are the different types of make are there in our dataset. And what is the count occurence of each make in the data?


# In[52]:


car.head(2)


# In[53]:


car['Make'].value_counts()


# In[54]:


car


# In[ ]:


# Filtering
# Show all the records where Origin in Asia of europe


# In[55]:


car.head(2)


# In[56]:


car[car['Origin'].isin(['Asia','Europe'])]


# In[ ]:


# Removing unwanted records
# Remove all the records(rows) where weight is above 4000


# In[73]:


car.head(2)


# In[59]:


car['Weight'] > 4000


# In[60]:


car[car['Weight'] > 4000]


# In[ ]:


# If want to remove the record of obove 4000


# In[72]:


import pandas as pd

car = pd.read_csv(r"C:\Users\Admin\Downloads\file.csv")
car[~(car['Weight'] > 4000)]


# In[ ]:


# Applying function on a column
# Increase all the values of MPG_City column by 3


# In[75]:


car.head(2)


# In[76]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[77]:


car


# In[78]:


car


# In[81]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+4)


# In[82]:


car

