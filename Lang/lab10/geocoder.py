import requests
from config import API_KEY

def get_json(geocode):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={geocode}&format=json"
    response = requests.get(geocoder_request)
    return response.json()

def get_coordinates(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    return list(map(lambda x: float(x), toponym_coodrinates.split()))

def get_district(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_district = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][1]["name"]
    return toponym_district

def get_postal_code(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return toponym_postal_code

def get_text_address(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_text_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    return toponym_text_address

def get_administartive_area(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_administartive_area = toponym["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]["AdministrativeArea"]["AdministrativeAreaName"]
    return toponym_administartive_area