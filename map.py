import folium

map = folium.Map(location=[31.452636429987884, 74.36261585417512], tiles = "Stamen Terrain")
map.save("map.html")