#!/bin/bash

set -eu

PYTHONPATH=./src \
    python3 -m unittest discover -s ./tests -p 'test_grou*.py'
