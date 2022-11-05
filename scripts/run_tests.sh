#!/bin/bash

set -eu

PYTHONPATH=./src \
    ./tests/test_endpoint.py
