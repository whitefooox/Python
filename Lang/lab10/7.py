import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=86.073238,55.359502&l=map&z=11&'
'pt=86.060298,55.344411,pmwts1~' #1 - ЖД Вокзал
'86.125416,55.388704,pmwts2~' #2 - Кемеровский кардиологический диспансер
'86.071911,55.375898,pmwts3~' #3 - Музей-заповедник «Красная Горка»
'86.078468,55.343819,pmwts4') #4 - Парк Ангелов
with open('result/7.png', 'wb') as file:
        file.write(response.content)