#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass


class CheckEndpoints(EndpointTestBaseClass):
    def test_all_freights_shown(self):
        response = self.endpoint_client.get('/api/v1/freight')
        self.assertEqual(len(response.json), 3)

    def test_adding_freight(self):
        response = self.endpoint_client.post('/api/v1/freight', json={
            'arrival_city_id': '23',
            'departure_city_id': '78',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['arrival_city_id'], '23')

    def test_freight_and_city_relation(self):
        response = self.endpoint_client.post('/api/v1/freight', json={
            'arrival_city_id': '23',
            'departure_city_id': '78',
        })

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['arrival_city_id'], '23')

        response = self.endpoint_client.get('/api/v1/freight')
        self.assertEqual(len(response.json), 4)
        self.assertEqual(response.json[3]['arrival_city']['name'], 'City D')
        self.assertEqual(response.json[3]['departure_city']['name'], 'City E')


if __name__ == '__main__':
    unittest.main()
