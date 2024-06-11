import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_order(params):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDERS_PATH,
                         params=params,
                         headers=data.headers)
