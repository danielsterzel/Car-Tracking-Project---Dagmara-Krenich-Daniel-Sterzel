import folium


m = folium.Map(location=[45.35, -121.6972], zoom_start=12)

m.add_child(folium.CircleMarker(location=(45.45, -121.6950)))

folium.Marker(
    location=(45.3488,-121.6932),
    tooltip='click me!',
    icon=folium.Icon(icon='fa-solid fa-car-side', color='red',prefix='fa')
).add_to(m)

m.save('map.html')
