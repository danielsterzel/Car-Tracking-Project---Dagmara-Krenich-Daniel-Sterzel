import folium
import os

m = folium.Map(location=(45.5236,-122.6750))  #opening for such coordinates
m.save('map.html') #saving to HTML File

file_path = os.path.abspath('map.html')
print(file_path)
