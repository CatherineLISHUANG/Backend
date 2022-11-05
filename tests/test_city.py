#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass


class CheckEndpoints(EndpointTestBaseClass):
    def test_all_citys_shown(self):
        response = self.endpoint_client.get('/api/v1/city')
        self.assertEqual(len(response.json), 5)

    def test_adding_city(self):
        response = self.endpoint_client.post('/api/v1/city', json={
            'name': 'City EXAMPLE',
            'post_code': 'City POSTCODE',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'City EXAMPLE')
        self.assertEqual(response.json['post_code'], 'City POSTCODE')


if __name__ == '__main__':
    unittest.main()
