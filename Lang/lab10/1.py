import requests

def save_map(coor, type, name, spn='0.01,0.01'):
    response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coor}8&spn={spn}&l={type}')
    with open(name, 'wb') as file:
        file.write(response.content)

kemsu = '86.090851,55.352041'
home = '86.092801,55.351035'
eiffel_tower = '2.294695,48.858717'
avacha_volcano = '159.057696,53.745054'
baikal = '107.673058,53.405332'
baikonur = '63.184111,46.198016'

save_map(kemsu, 'map', 'result/1/a.png')
save_map(home, 'map', 'result/1/b.png')
save_map(eiffel_tower, 'sat', 'result/1/c.jpg')
save_map(avacha_volcano, 'sat', 'result/1/d.jpg')
save_map(baikal, 'sat', 'result/1/e.jpg')
save_map(baikonur, 'sat', 'result/1/f.jpg')