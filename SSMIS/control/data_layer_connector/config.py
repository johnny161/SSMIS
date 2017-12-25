# -*- coding: utf-8 -*-

import json

def load_conf():
    #with open('config.json', 'r') as f:
    with open('control/data_layer_connector/config.json', 'r') as f:
        s = json.loads(f.read())
    return s
