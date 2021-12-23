from branca.element import IFrame
import folium
import pandas
from pandas.io import html

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
type = list(data["TYPE"])
elev = list(data["ELEV"])

html = """
    <b>Name: </b> %s
    <br>
    <b>Type: </b> %s
    <br>
    <b>Elevation: </b> %s
"""

def markerColor(elev):
    if elev > 4000:
        return "darkred"
    elif elev > 3000:
        return "red"
    elif elev > 2000:
        return "orange"
    elif elev > 1000:
        return "darkblue"
    else:
        return "blue"


map = folium.Map(location=[31.452636429987884, 74.36261585417512], tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, n, t, el in zip(lat, lon, name, type, elev):
    iframe = folium.IFrame(html=html % (n, t, el), width=200, height=60)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=markerColor(el))))

map.add_child(fg)

map.save("map.html")