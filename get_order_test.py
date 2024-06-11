import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Койфман Станислав, 17-я когорта — Финальный проект. Инженер по тестированию плюс
def get_params(track):
    params = data.params.copy()
    params["t"] = track
    return params


def test_positive_assert():
    order_response = sender_stand_request.post_new_order(data.order_body)
    assert order_response.status_code == 201
    assert order_response.json()["track"] != ""
    track_number = order_response.json()["track"]
    track_info_response = sender_stand_request.get_order(get_params(track_number))
    assert track_info_response.status_code == 200
    assert track_info_response.json()['order']["track"] == track_number

