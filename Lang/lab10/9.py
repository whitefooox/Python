from geocoder import get_json, get_coordinates

result = ''
northern_latitude = 90
cities = input('Введите список городов, через запятую:').split(',')

for city in cities:
    temp_northern_latitude = get_coordinates(get_json(city))[1]
    if temp_northern_latitude < northern_latitude:
        result = city
        northern_latitude = temp_northern_latitude

print('Южнее всех', result)