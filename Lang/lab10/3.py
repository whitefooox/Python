from geocoder import get_json, get_text_address, get_coordinates

json = get_json('Москва, Красная площадь, 1')
print('Адрес:', get_text_address(json))
print('Координаты:', get_coordinates(json))