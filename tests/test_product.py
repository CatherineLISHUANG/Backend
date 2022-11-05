#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass


class CheckEndpoints(EndpointTestBaseClass):
    def test_all_products_shown(self):
        response = self.endpoint_client.get('/api/v1/product')
        self.assertEqual(len(response.json), 3)

    def test_add_product(self):
        response = self.endpoint_client.post('/api/v1/product', json={
            'code': 'this-is-the-code',
            'name': 'my awesome product',
        })

        response = self.endpoint_client.get('/api/v1/product')
        self.assertEqual(len(response.json), 4)
        self.assertEqual(response.json[3]['name'], 'my awesome product')


if __name__ == '__main__':
    unittest.main()
