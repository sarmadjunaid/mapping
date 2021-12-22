import folium

map = folium.Map(location=[31.452636429987884, 74.36261585417512], tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[31.446479113224488, 74.40758976889724], popup="Sarmad's Home", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("map.html")