#!/usr/bin/env python
# coding: utf-8

# Done by Fatimah AlYami

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[265]:


PATH_CSV="./bank-additional.csv"
df=pd.read_csv(PATH_CSV)
df.shape


# ## 1. Histogram
# This histogram shows the age and marital status, it shows that people from the age 20 till almost 55 are single , and from the age 26 and above are married, and some people from 30 to almost 70 get divorced. 

# In[266]:


condition=(df['marital']=='married') | (df['marital']=='single')| (df['marital']=='divorced')
marital=df[condition]
plt.figure(figsize=(10,6), dpi=99)
sns.histplot(data=marital,
             x="age",
             hue="marital",
             binwidth=3,
             multiple="stack").set_title('Age and Marital Status')


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ## 2. Scatterplot. 
# This scatterplot shows the job, age, and the housing if the person have a house loan or not,admin from the age 29 to 39 have house loan more than any job category

# In[267]:


condition=(df['housing']=='yes') | (df['housing']=='no')
house=df[condition]

sns.relplot(
    x="age", 
    y="job", 
    hue="housing",
    alpha=.7, 
    palette="muted",
    height=7, 
    data=house
)

plt.title("Employee Job and does he/she have house loan or not?");
plt.ylabel('employee Job ')
plt.xlabel('Employee Age')


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ## 3. Barplot
# In this barplot, it shows the contact method and the number of contacts performed during the campaign, and the outcome of the campaign if its failure or success. As it shown in the barplot below, you can see that campaigns was performed by the telephone are 2.5 failed , and almost 1.6 was success. for the cellular, it was success 1.8 success and 1.6 failure. 

# In[268]:


condition=(df['poutcome']=='success') | (df['poutcome']=='failure')
outcome=df[condition]
plt.figure(figsize=(10,4))

plot3 = sns.catplot(
    data=outcome,
    kind="bar", 
    x="contact", 
    y="campaign", 
    hue="poutcome", 
    alpha=.8, 
    height=5,
    
)
plt.title("Was campaign success or failure ?");
plt.ylabel('Number of Contacts performed during the campaign')
plt.xlabel('contact communication type')


# ## 4. Pie Plot
# This pie plot explains the type of job that people go to bank and ask for loans in 2014,
# the blue-collar have the highest rate with 27%, technician with 18%, admin with 17%. The lowest rate is student,retired,unemployed with 1%

# In[269]:


condition3=(df['loan']=='yes') & (df['job']!='unknown')
loan=df[condition3]

plt.figure(figsize=(14,15),dpi=100)
loan["job"].value_counts(normalize=True).plot(
    kind="pie",
    legend=True,
    autopct='%.f%%',
)
plt.title("Type of Job ",c="black")
plt.ylabel(" ")

