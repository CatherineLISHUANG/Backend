#!/usr/bin/env python3
import random
import uuid
import os
import json
from faker import Faker
import requests


def get_rand_id():
    return str(uuid.uuid4())


APP_HOST = os.getenv('APP_HOST', 'http://127.0.0.1:5005')


def generate_cities():
    fake = Faker()
    cities = [{
        'id': get_rand_id(),
        'name': fake.city(),
        'post_code': fake.postcode(),
    } for _ in range(os.getenv('NUM_CITY', 10))]
    return cities


def generate_freights(cities):
    fake = Faker()
    freights = [{
        'id': get_rand_id(),
        'departure_city_id': choose_rand_id(cities),
        'arrival_city_id': choose_rand_id(cities),
        'pre_calc_distance': random.randint(100, 1000),
        'pre_calc_weight': random.randint(100, 1000),
        'pre_calc_volume': random.randint(100, 1000),
        'pre_calc_price': random.randint(100, 1000),
        'date': fake.date(),
    } for _ in range(os.getenv('NUM_FREIGHT', 10))]

    return freights

def generate_customers():
    fake= Faker()
    return [
        {
            'id': get_rand_id(),
            'code': random.randint(100, 1000),
            'name': fake.name(),
            'email_address': fake.email(),
        } for _ in range(os.getenv('NUM_CUSTOMER', 10))
    ]

def generate_products():
    fake= Faker()
    return [
        {
            'id': get_rand_id(),
            'code': random.randint(100, 1000),
            'name': fake.catch_phrase(),
            'product_class': fake.company(),
            'price': random.randint(100, 1000),
        } for _ in range(os.getenv('NUM_PRODUCT', 10))
    ]


def generate_orders(customers, products):
    fake= Faker()
    return [
        {
            'id': get_rand_id(),
            'date': fake.date(),
            'product_quantity': random.randint(100, 1000),
            'customer_id': choose_rand_id(customers),
            'product_id': choose_rand_id(products),
        } for _ in range(os.getenv('NUM_ORDER', 10))
    ]



def add_resource(endpoint, data_as_dict):
    payload= json.dumps(data_as_dict)
    url= f'{APP_HOST}/api/v1/{endpoint}'
    response= requests.post(url, json=payload)
    print(response.json())

def choose_rand_id(items):
    return random.choice([c['id'] for c in items])


def main():
    customers= generate_customers()
    products= generate_products()
    orders= generate_orders(customers, products)

    cities= generate_cities()
    freights= generate_freights(cities)


    for customer in customers:
        add_resource('customer', customer)

    for product in products:
        add_resource('product', product)

    for order in orders:
        add_resource('order', order)

    for city in cities:
        add_resource('city', city)

    for freight in freights:
        add_resource('freight', freight)


if __name__ == '__main__':
    main()
