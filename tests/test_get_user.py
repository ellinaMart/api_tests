# -*- coding: utf-8 -*-
import requests
import os
import json

with open(os.path.join(os.path.dirname('api_tests'), 'config.json')) as config_file:
    config = json.load(config_file)

def test_get_user():
    user_ids = []
    # для каждой страницы юзеров отправляем запрос на список юзеров на каждой странице
    for page in [1,2,3]:
        params = {
            "page" : page
        }
        resp = requests.get(config["url_users"], params)
        assert resp.status_code == 200

        # проверяем, что возвращается верная страница
        json_data = json.loads(resp.text)
        assert json_data["page"] == page

        # собираем id всех юзеров в массив
        for i in json_data["data"]:
            user_ids.append(i["id"])

        # для каждого id юзера из массива отправляем запрос на получение информации о каждом юзере
    for id in user_ids:
        resp_user = requests.get(config["url_users"] + "/" + str(id))
        assert resp_user.status_code == 200

        # проверяем, что возвращается верный id
        json_data = json.loads(resp_user.text)
        assert json_data["data"]["id"] == id

def test_get_user_negative():
    # Проверяем, что при запросе юзера с несуществующим id вернет 404
    resp_user = requests.get(config["url_users"] + "/23")
    assert resp_user.status_code == 404







