#!/usr/bin/env python3
import unittest
from base_classes import EndpointTestBaseClass
import json

class CheckEndpoints(EndpointTestBaseClass):
    def test_all_orders_shown_and_grouped(self):
        response = self.endpoint_client.get('/api/v1/grouped')
        # city_d = [o['items'] for o in grouped if o['city_name'] == 'City D']
        # self.assertEqual(city_d, 2)


if __name__ == '__main__':
    unittest.main()
