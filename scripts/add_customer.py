#!/usr/bin/env python3

import pandas as pd
import json
import requests

data = pd.read_csv('./sandbox/data/Orders.csv',delimiter=',')
df = pd.DataFrame(data)

customer_set = set(df['CustomerCode'])

def add_customer(customer):
	payload = json.dumps(customer)
	resp = requests.post("http://127.0.0.1:5005/api/v1/customer", json=payload)
	print(resp.json())

for i in customer_set:
    # code = customer_set[i]
    my_customer = {
        'code': i,
        'name': '',
        'email_address': '',
    }
    add_customer(my_customer)