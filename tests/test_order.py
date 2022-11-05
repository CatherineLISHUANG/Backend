#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass


class CheckEndpoints(EndpointTestBaseClass):
    def test_all_orders_shown(self):
        response = self.endpoint_client.get('/api/v1/order')
        self.assertEqual(len(response.json), 4)

    def test_order_relations(self):
        response = self.endpoint_client.post('/api/v1/order', json={
            'city_id': '17',
            'product_id': '78695',
            'customer_id': '32',
        })

        response = self.endpoint_client.get('/api/v1/order')
        self.assertEqual(len(response.json), 5)
        self.assertEqual(response.json[4]['customer']['name'], 'Michael Steel')
        self.assertEqual(response.json[4]['city']['name'], 'City C')
        self.assertEqual(response.json[4]['product']['name'], 'my product 3')


if __name__ == '__main__':
    unittest.main()
