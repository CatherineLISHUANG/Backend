#!/usr/bin/env python3

import pandas as pd
import json
import requests

data = pd.read_csv('./sandbox/data/Freight.csv',delimiter=';')
data2 = pd.read_csv('./sandbox/data/Orders.csv',delimiter=',')
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

city_set_1 = set(df['Departure'])
city_set_2 = set(df['Arrival'])
city_set_order = set(df2['Arrival'])

city = city_set_1.union(city_set_2.union(city_set_order))

post=[]# just the post code


def add_city_to_db(city_dictionary):
    payload = json.dumps(city_dictionary,ensure_ascii=False)
    response = requests.post("http://127.0.0.1:5005/api/v1/city", json=payload)
    print(response.json())

for i in city:
	if i in city_set_1:
		post = list(df.loc[df['Departure']==i,'DeparturePostCode'])
		key_value ={'name': i, 'post_code': post[0]}
		add_city_to_db(key_value)
	else:
		if i in city_set_2:
		    post = list(df.loc[df['Arrival']==i,'ArrivalPostCode'])
		    key_value ={'name': i, 'post_code': post[0]}
		    add_city_to_db(key_value)
		else:
			post = list(df2.loc[df2['Arrival']==i,'ArrivalPostCode'])
			key_value ={'name': i, 'post_code': post[0]}
			add_city_to_db(key_value)

# for i in city_set_1:
# 	post = list(df.loc[df['Departure']==i,'DeparturePostCode'])
# 	key_value ={'name': i, 'post_code': post[0]}
# 	add_city_to_db(key_value)

# for i in city_set_2:
# 	post = list(df.loc[df['Arrival']==i,'ArrivalPostCode'])
# 	key_value ={'name': i, 'post_code': post[0]}
# 	add_city_to_db(key_value)

