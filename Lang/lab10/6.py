import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=133.795393,-25.6947768&l=sat&z=4')
with open('result/6.jpg', 'wb') as file:
        file.write(response.content)