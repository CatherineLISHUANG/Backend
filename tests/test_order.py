#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass
import json

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

    def test_getting_order_by_id(self):
        response = self.endpoint_client.get('/api/v1/order?id=1547')
        self.assertEqual(response.json['id'], '1547')
        self.assertEqual(response.json['product']['price'], 5400)

    def test_order_update(self):
        response = self.endpoint_client.get('/api/v1/order?id=1547')
        my_order = response.json
        self.assertEqual(my_order['id'], '1547')
        self.assertEqual(my_order['status'], 'PENDING')

        status_update_payload = {
            'order_id': my_order['id'],
            'new_status': 'APPROVED'
        }
        response = self.endpoint_client.put('/api/v1/order', json=status_update_payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['status'], 'APPROVED')


if __name__ == '__main__':
    unittest.main()
