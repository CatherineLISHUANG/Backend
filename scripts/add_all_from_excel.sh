#!/bin/bash

set -eu

./scripts/add_city.py
./scripts/add_customer.py
./scripts/add_product.py

./scripts/add_freight.py
./scripts/add_order.py
