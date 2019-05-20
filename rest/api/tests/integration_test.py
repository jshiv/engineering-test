
import requests
import json
import pytest

url = 'http://localhost:8080'

def test_find():
  data = {"type": "Point", "coordinates": [-73.748751, 40.9185483]}
  r = requests.post(url+'/find/100', json=json.dumps(data))
  assert json.loads(r.content) == ['f1650f2a99824f349643ad234abff6a2']



def test_stats_get():
  r = requests.get(url+'/stats/f1650f2a99824f349643ad234abff6a2/100')
  assert json.loads(r.content) == [{'id': 'f1650f2a99824f349643ad234abff6a2',
    'parcel_area': 911.830634661019,
    'building_area': 265.53891967237,
    'building_distance_to_center': 1.39291243,
    'zone_density': 0.00850243474131589}]


