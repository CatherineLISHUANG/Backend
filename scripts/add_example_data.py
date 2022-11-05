#!/usr/bin/env python3
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


def add_resource(endpoint, data_as_dict):
    payload = json.dumps(data_as_dict)
    url = f'{APP_HOST}/api/v1/{endpoint}'
    response = requests.post(url, json=payload)
    print(response.json())


def main():

    cities = generate_cities()

    for city in cities:
        add_resource('city', city)


if __name__ == '__main__':
    main()
