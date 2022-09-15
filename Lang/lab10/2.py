from geocoder import get_json, get_coordinates, get_district, get_postal_code

geocode = ['Якутск', 'Магадан', 'Торонто', 'Хабаровск', 'Уфа', 'Нижний новгород', 'Калининград', 'Кемерово', 'Кемерово, ул.Красная, 6']

yakutsk_coor = get_coordinates(get_json(geocode[0]))
magadan_coor = get_coordinates(get_json(geocode[1]))

print('a) ', end='')
if yakutsk_coor[1] > magadan_coor[1]:
    print('Якутск севернеее Магадана')
else:
    print('Магадан севернее Якутска')

kemerovo_coor = get_coordinates(get_json(geocode[7]))
toronto_coor = get_coordinates(get_json(geocode[2]))

print('b) ', end='')
if kemerovo_coor[1] < toronto_coor[1]:
    print('Кемерово южнее Торонто')
else:
    print('Торонто южнее Кемерово')

print('c) ', end='')
for i in range(3, 8):
    district = get_district(get_json(geocode[i]))
    print(geocode[i], district, sep=' - ')

print('d) ', end='')
print(get_postal_code(get_json(geocode[8])))