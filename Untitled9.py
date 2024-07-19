#!/usr/bin/env python
# coding: utf-8

# In[8]:


import json
import pandas as pd


# In[3]:


f= open("C:\\Users\\Lenovo\\Downloads\\DataEngineeringQ2.json")


# In[4]:


data = json.load(f)


# In[11]:


for i in data:
    print(i)


# In[ ]:





# In[107]:


df = pd.read_json("C:\\Users\\Lenovo\\Downloads\\DataEngineeringQ2.json")


# In[108]:


df


# In[109]:


df.info()


# In[110]:


df.isnull().sum()


# In[111]:


df['patientDetails'][1]


# In[112]:


df['patientDetails'][3]


# In[ ]:





# In[113]:


df['consultationData'][0:30]


# In[114]:


df['consultationData'][0]['medicines']


# In[67]:


for i in range(30):
    print (df['consultationData'][:]['medicines'])


# In[86]:


df['consultationData'][0]


# In[95]:



medicines_list = []

for index, row in df.iterrows():
    medicines = row['consultationData']['medicines']
    for medicine in medicines:
        medicines_list.append({
            'row_index': index,
            'medicineId': medicine['medicineId'],
            'medicineName': medicine['medicineName'],
            'medicineNameStrengthType': medicine['medicineNameStrengthType'],
            'frequency': medicine['frequency'],
            'duration': medicine['duration'],
            'durationIn': medicine['durationIn'],
            'instruction': medicine['instruction'],
            'isActive': medicine['isActive']
        })

medicines_df = pd.DataFrame(medicines_list)

print(medicines_df)


# In[96]:


medicines_df


# In[97]:


medicines_df.info()


# In[98]:


medicines_df['medicineName'].unique()


# In[99]:


medicines_df['medicineName']


# In[101]:


import pandas as pd
from collections import Counter

df = pd.DataFrame({
    'consultationData': [
        
    ]
})

medicine_names = []

for index, row in df.iterrows():
    medicines = row['consultationData']['medicines']
    for medicine in medicines:
        medicine_names.append(medicine['medicineName'])

medicine_counts = Counter(medicine_names)

sorted_medicine_counts = sorted(medicine_counts.items(), key=lambda x: x[1], reverse=True)

third_most_frequent_medicine = sorted_medicine_counts[2][0] if len(sorted_medicine_counts) >= 3 else None

print("3rd most ", third_most_frequent_medicine)


# In[ ]:





# In[105]:



import pandas as pd

df = 

active_count = 0
inactive_count = 0

for index, row in df.iterrows():
    medicines = row['consultationData']['medicines']
    for medicine in medicines:
        if medicine['isActive']:
            active_count += 1
        else:
            inactive_count += 1

total_medicines = active_count + inactive_count

active_percentage = (active_count / total_medicines) * 100
inactive_percentage = (inactive_count / total_medicines) * 100

print(f"Active : {active_percentage:.2f}%")
print(f"Inactive : {inactive_percentage:.2f}%")


# In[ ]:




