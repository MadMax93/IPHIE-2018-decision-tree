
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("diabetic_data.csv")


# In[3]:


data.head()


# In[4]:


##drop the weight and payer_code column due to high rates of missing data
data = data.drop(['weight', 'payer_code'], axis=1)


# In[5]:


len(data)


# In[6]:


##Omit discharge disposition ids that correspond to hospice or death. These include: 11, 13, 14, 19, 20, 21.
a = [11, 13, 14, 19, 20, 21]
data = data[~data.discharge_disposition_id.isin(a)]


# In[7]:


len(data)


# In[8]:


##make function to recode readmission, 0 is no readmission or >30 days, <30 days is an early readmission
def recode(x):
    if x == 'NO'or x == '>30':
        return 0
    else:
        return 1


# In[9]:


##recode readmission
data['readmitted'] = data['readmitted'].apply(recode)


# In[10]:


data.head()


# In[11]:


data2 = data.loc[data.groupby("patient_nbr")["encounter_id"].idxmin()]


# In[14]:


len(data2)


# In[15]:


data2 = data2.reset_index()


# In[19]:


data2["patient_nbr"] = data2["index"]


# In[20]:


data2.head()


# In[26]:


data2 = data2.drop(["index"], axis=1)
data2.head()


# In[27]:


data2.to_csv("19062018_dataset_cleaned.csv", sep=",")


# In[84]:


unique_patients = list(set(data.patient_nbr.values))


# In[93]:


import numpy as np


# In[108]:



test = list()
for pat in unique_patients:
    rows = data.loc[data["patient_nbr"] == pat]
    if len(rows) > 1:
        lowest = np.min(rows["encounter_id"].values)
        selection = rows.loc[rows["encounter_id"] == lowest]
        test.append(selection)
        continue;
    test.append(rows)


# In[ ]:


len(test)


# In[ ]:


test[0]


# In[ ]:



df_result = pd.DataFrame(test,columns=data.columns)


# In[111]:


df_result.head()


# In[82]:


data2.head()


# In[86]:


df_counts = pd.DataFrame(data['patient_nbr'].value_counts()).reset_index()


# In[87]:


df_counts.head()


# In[88]:


df_counts = df_counts.loc[df_counts["patient_nbr"] > 1]
data2 = data.loc[data["patient_nbr"].isin(df_counts["index"])]


# In[91]:


data2.head()


# In[ ]:


data["multiple_visits"] = data.loc[data["patient_nbr"].isin(data2["patient_nbr"])]


# In[5]:


##
data1 = open('temp1_new.csv', 'r')
line1 = data1.readline()
pt_encounter = dict()
for line in data1:
    items = line.strip('\n').split(',')
    encounter_id = items[0]
    pt_id = items[1]
    if pt_id not in pt_encounter:
        pt_encounter[pt_id] = encounter_id
    elif int(items[0]) < int(pt_encounter[pt_id]):
        pt_encounter[pt_id] = items[0]
print ('finish part1')
data1.close() 
print (len(pt_encounter))         
        


# In[6]:


pt_encounter

