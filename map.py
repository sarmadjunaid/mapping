import folium
import pandas
from pandas.io import html

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
type = list(data["TYPE"])

map = folium.Map(location=[31.452636429987884, 74.36261585417512], tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, n, t in zip(lat, lon, name, type):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(html=f"<b>Name:</b> {n} <br> <b>Type:</b> {t}", max_width=80), icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("map.html")