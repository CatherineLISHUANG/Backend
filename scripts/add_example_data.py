#!/usr/bin/env python3
import uuid
import os
import json
from faker import Faker
import requests

def get_rand_id():
    return str(uuid.uuid4())


def generate_cities():
    total = 20

    fake = Faker()
    cities = [{
        'id': get_rand_id(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
    } for _ in range(total)]
    return cities

def add_city_to_db(city_dictionary):
    '''
    city_dictionary

    {
        'name': '...',
        'post_code': '...',
    }
    '''
    payload = json.dumps(city_dictionary)
    url = f'http://127.0.0.1:5005/api/v1/city'
    response = requests.post(url, json=payload) # need to debug why
    print(response.json())


def main():

    users = generate_cities()

    for user in users:
        create_freight(user)

if __name__ == '__main__':
    main()
