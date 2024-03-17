#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 


# In[2]:


#pip install matplotlib


# In[3]:


get_ipython().system('dir')


# In[4]:


df = pd.read_csv('Bank Target Marketing Dataset.csv')


# In[5]:


Bank_Target = df
df


# In[6]:


df.isna()


# In[7]:


df.isna().any()


# In[8]:


#df.drop(['default'], axis = 1, inplace= True)
df.drop(['default'], axis=1, inplace= True)


# In[9]:


df


# In[10]:


df.duplicated().nunique()


# In[11]:


df.duplicated().any()


# In[12]:


df.job.value_counts()


# In[13]:


top_5_jobs = df['job'].value_counts().head(5)
print(top_5_jobs)


# In[44]:


plt.figure(figsize=(10, 6))
top_5_jobs.plot(kind='pie', color='skyblue')
plt.title('Top 5 Job Counts')
plt.xlabel('Job')
plt.ylabel('Count')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if necessary
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[14]:


Bank_Target.iloc[:,[1,2]]


# In[15]:


Bank_Target = Bank_Target.drop_duplicates()

Bank_Target 


# In[16]:


Bank_Target.marital.value_counts()


# In[45]:


print("Marital value counts:")
print(Bank_Target.marital.value_counts())
print()

# View value counts for the 'deposit' column
print("Deposit value counts:")
print(Bank_Target.deposit.value_counts())
print()

# View value counts for the 'age' column
print("Age value counts:")
print(Bank_Target.age.value_counts())


# In[60]:


fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot value counts for 'marital' column
Bank_Target.marital.value_counts().plot(kind='pie', ax=axs[0], color='olive')
axs[0].set_title('Marital Status')
axs[0].set_xlabel('Marital Status')
axs[0].set_ylabel('Count')

# Plot value counts for 'deposit' column
Bank_Target.deposit.value_counts().plot(kind='bar', ax=axs[1], color='orange')
axs[1].set_title('Deposit')
axs[1].set_xlabel('Deposit')
axs[1].set_ylabel('Count')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()


# In[59]:


# Set up subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plot top 5 age counts
top_age = df['age'].value_counts().head(5)
top_age.plot(kind='barh', ax=axs[0], color='skyblue')
axs[0].set_title('Top 5 Age Counts')
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Count')

# Plot value counts for 'education' column
Bank_Target.education.value_counts().plot(kind='bar', ax=axs[1], color='red')
axs[1].set_title('Education')
axs[1].set_xlabel('Education Level')
axs[1].set_ylabel('Count')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()


# In[18]:


Bank_Target.deposit.value_counts()


# In[19]:


Bank_Target.age.value_counts()
#Bank_Target.deposit.value_counts()


# In[20]:


top_age = df['age'].value_counts().head(5)
print(top_age)


# In[21]:


Bank_Target.education.value_counts()


# In[22]:


df = Bank_Target
Bank_Target.groupby('education')[['balance', 'age']].mean()
# Example DataFrame
df = pd.DataFrame({'Education': [1, 2, 3, 4, 5],
                   'Age': [5, 4, 3, 2, 1]})


# In[23]:


df = Bank_Target
Bank_Target.groupby('deposit').agg({'balance': 'mean', 'age': 'mean' })
                                              


# In[24]:


Bank_Target.groupby('job').agg({'balance': 'mean', 'age': 'mean' })


# In[25]:


#def Bank_Target(df, job_column, deposit_column, marital_column, age_column):
#    for c in df[job_column].unique():
#        mean_deposit = df[df[job_column] == c][deposit_column].mean()
#       print(f"The mean deposit from occupation {c} was: {mean_deposit:.2f}")

# Example usage:
#Bank_Target(Bank_Target, 'job', 'deposit', 'marital', 'age')


# In[26]:


def aggregate(df: pd.DataFrame, aggregate_columns: list, aggregate_dict: dict) -> pd.DataFrame:
    
    df2 = df.copy()
    final_df = df2.groupby(aggregate_columns).agg(aggregate_dict)
    
    return final_df


# In[27]:


df.head()


# In[28]:


aggregate(df, ["job","marital","deposit"], {"balance":'mean',"duration": "mean"})


# In[29]:


get_ipython().system('dir')


# In[ ]:





# In[30]:


aggregate(df, ["age","marital","deposit"], {"balance":'mean',"duration": "mean"})


# In[ ]:




