# -*- coding: utf-8 -*-
import requests
import os
import json
from .testdata import test_data

with open(os.path.join(os.path.dirname('api_tests'), 'config.json')) as config_file:
    config = json.load(config_file)

def test_add_user():
    for data in test_data:
        resp = requests.post(config["url_users"], params=data)
        assert resp.status_code == 201


def test_update_user():
    resp = requests.put(config["url_users"] + "/2", test_data[0])
    assert resp.status_code == 200

def test_delete_user():
    resp = requests.delete(config["url_users"] + "/2")
    assert resp.status_code == 204
