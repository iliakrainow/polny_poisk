import sys
from io import BytesIO
import requests
from PIL import Image
from toponym_envelope import get_toponym_envelope

# python search.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass
# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
    "GeoObject"
]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]


ll, spn = get_toponym_envelope(toponym)
map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    "pt": toponym_coodrinates.replace(" ", ","),
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(response.content)).show()
input()
