#!/usr/bin/env python3

import pandas as pd
import json
import requests

data = pd.read_csv('./sandbox/data/Products.csv',delimiter=';')
df = pd.DataFrame(data)


def add_product(product):
	payload = json.dumps(product)
	resp = requests.post("http://127.0.0.1:5005/api/v1/product", json=payload)
	# print(resp.json())

for i in range(len(df)):
    row = list(df.iloc[i])
    my_product = {
        'code': str(row[1]),
        'product_class': str(row[0]),
        'name': str(row[11]),
        'price': str(row[2]),
        'sales_unit': str(row[3]),
        'weight_kg': str(row[4]),
        'total_volume_m3': str(row[6]*row[7]*row[8]),
    }
    add_product(my_product)