#!/usr/bin/env python3

import pandas as pd
import json
import requests
from faker import Faker

data = pd.read_csv('./sandbox/data/Orders.csv',delimiter=',')
df = pd.DataFrame(data)

customer_set = set(df['CustomerCode'])

def add_customer(customer):
	payload = json.dumps(customer)
	resp = requests.post("http://127.0.0.1:5005/api/v1/customer", json=payload)
	print(resp.json())

for i in customer_set:
    # code = customer_set[i]
    fake = Faker()
    fake_name = fake.name()
    company_name = fake.company().replace(" ", "_").lower().replace(",", "").replace("-", "_")
    my_customer = {
        'code': i,
        'name': fake_name,
        'email_address': f'{fake_name.replace(" ", ".").lower()}@{company_name}.com',
    }
    add_customer(my_customer)