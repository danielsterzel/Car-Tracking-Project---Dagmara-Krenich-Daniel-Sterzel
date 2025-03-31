
import folium
import os

m = folium.Map(location=(45.5236,-122.6750))
m.save('map.html')


file_path = os.path.abspath('map.html')
print(file_path)
