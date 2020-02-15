#!/bin/bash
python3 -m virtualenv --python="/usr/bin/python3" env && \
 source env/bin/activate && \
 python3 -m pip install -r requirements.txt