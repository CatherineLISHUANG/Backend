#!/usr/bin/env python3

import pandas as pd
import json
import requests
import datetime

data = pd.read_csv('./sandbox/data/Orders.csv',delimiter=',')
df = pd.DataFrame(data)


all_customers = requests.get('http://127.0.0.1:5005/api/v1/customer').json()
all_cities = requests.get('http://127.0.0.1:5005/api/v1/city').json()
all_products = requests.get('http://127.0.0.1:5005/api/v1/product').json()

#print("====> citites:", all_cities)

def get_customer_id(customer):
    try:
        filtered = [c for c in all_customers if c['code'] == customer]
        return filtered[0]['id']
    except:
        raise Exception(f'Failed to get customer id: {customer}')

def get_city_id(city):
    try:
        filtered = [c for c in all_cities if c['name'] == city]
        print(filtered)
        return filtered[0]['id']
    except:
        raise Exception(f'Failed to get city id: {city}')


def get_product_id(product):
    try:
        filtered = [p for p in all_products if p['code'] == product]
        return filtered[0]['id']
    except:
        raise Exception(f'Failed to get product id: {product}')


def add_order(order):
    payload = json.dumps(order)
    response = requests.post("http://127.0.0.1:5005/api/v1/order",json=payload)
    print(response.json())

for i in range(len(df)):
    row = list(df.iloc[i])
    #my_date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
    my_order = {
        'code': str(row[1]),
        'date': row[2],
        'product_quantity': str(row[5]),
        'customer_id': get_customer_id(str(row[3])),
        'city_id': get_city_id(str(row[7])),
        'product_id': get_product_id(row[4]),
    }
    add_order(my_order)

