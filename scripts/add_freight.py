#!/usr/bin/env python3

import pandas as pd
import json
import requests
import datetime

data = pd.read_csv('./sandbox/data/Freight.csv',delimiter=';')
df = pd.DataFrame(data)


all_cities = requests.get('http://127.0.0.1:5005/api/v1/city').json()


def get_city_id(city):
	try:
		filtered = [c for c in all_cities if c['name'] == city]
		return filtered[0]['id']
	except:
		raise Exception(f'Failed to get city id: {city}')



def add_freight(freight):
	payload = json.dumps(freight)
	resp = requests.post("http://127.0.0.1:5005/api/v1/freight", json=payload)
	print(resp.json())

for i in range(len(df)):
    freight = list(df.iloc[i])
    our_date = datetime.datetime.strptime(freight[9], "%d.%m.%Y")
    my_freight = {
        'code': str(i),
        'departure_city_id': get_city_id(freight[1]),
        'arrival_city_id': get_city_id(freight[3]),
        'pre_calc_distance': str(freight[5]),
        'pre_calc_weight': str(freight[6]),
        'pre_calc_volume': str(freight[7]),
        'pre_calc_price': str(freight[8]),
        'date': datetime.datetime.strftime(our_date, "%Y-%m-%d")
    }
    add_freight(my_freight)
