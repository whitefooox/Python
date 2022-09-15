import requests

response = requests.get('https://static-maps.yandex.ru/1.x/?ll=86.087314,55.354968&l=map&z=6&'
'pl=c:C70039C0,w:4,86.086847,55.355198,86.162243,54.663609,87.136053,53.757553,87.983137,52.929298')

with open('result/8.png', 'wb') as file:
    file.write(response.content)