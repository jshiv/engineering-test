#!/usr/bin/env python
# coding: utf-8

# In[51]:


import requests
import json
url = 'http://localhost:5000'


# In[52]:


data = {"type": "Point", "coordinates": [-73.748751, 40.9185483]}
json.dumps(data)


# In[56]:


r = requests.post(url+'/find/100', json=json.dumps(data))
assert json.loads(r.content) == ['f1650f2a99824f349643ad234abff6a2']


# In[54]:


json.loads(r.content)


# In[78]:


r = requests.get(url+'/stats/f1650f2a99824f349643ad234abff6a2/100')
assert json.loads(r.content) == [{'id': 'f1650f2a99824f349643ad234abff6a2',
  'parcel_area': 911.830634661019,
  'building_area': 265.53891967237,
  'building_distance_to_center': 1.39291243,
  'zone_density': 0.00850243474131589}]


# In[ ]:




