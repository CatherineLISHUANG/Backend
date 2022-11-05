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
    total = 20

    fake = Faker()
    cities = [{
        'id': get_rand_id(),
        'name': fake.city(),
        'post_code': fake.postcode(),
    } for _ in range(total)]
    return cities

def get_rand_city_id(cities):
    return random.choice([c['id'] for c in cities])

def generate_freights(cities):
    total = 100
    fake = Faker()
    freights = [{
        'id': get_rand_id(),
        'departure_city_id': get_rand_city_id(cities),
        'arrival_city_id': get_rand_city_id(cities),
        'pre_calc_distance': random.randint(100, 1000),
        'pre_calc_weight': random.randint(100, 1000),
        'pre_calc_volume': random.randint(100, 1000),
        'pre_calc_price': random.randint(100, 1000),
        'date': fake.date(),
    } for _ in range(total)]

    return freights


def add_resource(endpoint, data_as_dict):
    payload = json.dumps(data_as_dict)
    url = f'{APP_HOST}/api/v1/{endpoint}'
    response = requests.post(url, json=payload)
    print(response.json())


def main():

    cities = generate_cities()

    for city in cities:
        add_resource('city', city)

    freights = generate_freights(cities)
    for freight in freights:
        add_resource('freight', freight)


if __name__ == '__main__':
    main()
