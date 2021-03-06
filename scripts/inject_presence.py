#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import with_statement
import paho.mqtt.client as mqtt
import json
import time

######## r3 ############

def sendR3Message(client, structname, datadict):
    client.publish(structname, json.dumps(datadict), 0, True)

#Start zmq connection to publish / forward sensor data
client = mqtt.Client()
client.connect("mqtt.realraum.at", 1883, 60)

#listen for sensor data and forward them
sendR3Message(client,"realraum/metaevt/presence",{"Present":True,"Ts":int(time.time())})
client.loop_write()
client.loop_read()
client.loop_misc()
client.disconnect()

