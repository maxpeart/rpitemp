#!/usr/bin/env python
import platform
from datetime import datetime
import time
import os

from gpiozero import CPUTemperature

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

database_url = os.environ['DATABASE_URL']
service_account = os.environ['SERVICE_ACCOUNT']
interval = int(os.environ['INTERVAL'])
hostname = os.environ['HOST_NAME']
# 'HOST_NAME={{.Node.Hostname}}'
print(f"Running with database: {database_url}")
print(f"Running with config: {service_account}")
print(f"Every: {interval}s on host: {hostname}")

cred = credentials.Certificate(service_account)
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': database_url
})

def push_value(temp):
    ref = db.reference('server/saving-data/temp/'+hostname)
    timestamp = datetime.now().isoformat(timespec='seconds')
    # [START push_value]
    # posts_ref = ref.child('posts')

    # We can also chain the two calls together
    ref.push().set({
        'temp': temp,
        'timestamp': timestamp
    })
    # [END push_value]

while True:
    cpu = CPUTemperature()
    print(f"temp {cpu.temperature}")
    push_value(cpu.temperature)
    time.sleep(interval)