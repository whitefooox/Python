from geocoder import get_json, get_administartive_area

geocode = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

for address in geocode:
    print(address, get_administartive_area(get_json(address)), sep=' - ')