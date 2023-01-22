from textwrap import fill
from turtle import fillcolor
import folium


# Создаем объек folium с координатами Нижнего Новгорода в оптимальном зуме
m = folium.Map(
    location=[56.32463861979883,43.99471526174922],
    tiles=None,
    min_zoom=11
)

# Создаем два слоя карты
folium.raster_layers.TileLayer("OpenStreetMap", name='Уличная карта').add_to(m)
folium.raster_layers.TileLayer("Stamen Terrain", name='Физическая карта', show=False).add_to(m)

# Создаем группу объектов
feature_group = folium.FeatureGroup(name='Стены Нижегородского Кремля')


# Добавляем пару маркеров
folium.Marker(
    [56.328324, 43.961313],
    popup='<b>Нижегородская Ярмарка</b><br><i>Совнаркомовская улица, 13</i>',
    tooltip='Нижегородская Ярмарка',
    icon=folium.Icon(color='orange')
).add_to(m)


folium.Marker(
    [56.327851, 44.001700],
    popup='<b>Нижегородский Кремль</b><br><i>Площадь Минина</i>',
    tooltip='Нижегородский Кремль',
    icon=folium.Icon(color='darkred')
).add_to(m)

# Создаем полигон стен Кремля
ls = folium.Polygon(
    locations=[
        [56.32582, 43.99897],
        [56.32567, 44.0014],
        [56.32705, 44.00567],
        [56.33011, 44.0089],
        [56.33075, 44.00625],
        [56.33081, 44.00346],
        [56.33053, 44.00179],
        [56.32987, 43.99962],
        [56.32882, 43.99887],
        [56.32878, 43.998],
        [56.32757, 43.99726],
        [56.32581, 43.99895],
        ],
        color = 'darkred',
        fill = True,
        fill_color = '#A62000',
        fill_opacity=0.2
)

ls.add_child(folium.Popup('Стены Нижегородского Кремля'))
feature_group.add_child(ls)
feature_group.add_to(m)

# Создаем управление слоями
folium.LayerControl(collapsed=False).add_to(m)

# Сохраняем объект folium в html
m.save('index.html')
