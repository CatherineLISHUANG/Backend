#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass


class CheckEndpoints(EndpointTestBaseClass):
    def test_all_customers_shown(self):
        response = self.endpoint_client.get('/api/v1/customer')
        self.assertEqual(len(response.json), 5)

    def test_adding_customer(self):
        response = self.endpoint_client.post('/api/v1/customer', json={
            'name': 'ExampleName',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'ExampleName')


if __name__ == '__main__':
    unittest.main()
