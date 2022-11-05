import pandas as pd
import json
import requests

data = pd.read_csv('./sandbox/data/Freight.csv',delimiter=';')
df = pd.DataFrame(data)



all_cities = requests.get('http://127.0.0.1:5005//api/v1/city')

parsed = all_cities.json()
print(type(parsed))
for entity in parsed:
	print(entity)

def get_city_id(city):
	try:
		filtered = [c for c in parsed if c['name'] == city]
		print('==>', filtered)
		return filtered[0]['id']
	except:
		raise Exception(f'Failed to get city id: {city}')



def add_freight(freight):
	print('==> type is: ', type(freight))
	payload = freight
	print('before:', payload)
	# if isinstance(freight, dict):
	payload = json.dumps(freight)
	print('after: ', payload)
	response = requests.post("http://127.0.0.1:5005/api/v1/city", json=payload)
	# print(response.json())
	

for i in range(len(df)):
    freight = list(df.iloc[i])
    my_freight = {
        'code': i,
        'departureID': get_city_id(freight[1]),
        'arrivalID': get_city_id(freight[3]),
        'distance': freight[5],
        'weight': freight[6],
        'volume': freight[7],
        'price': freight[8],
        'date': freight[9]
    }
    add_freight(my_freight)

