import folium 
import pandas as pd

data = pd.read_csv('city_accident_data.csv')

def get_marker_color(accident_count, threshold=150):
    return 'red' if accident_count > threshold else 'green'

for _, row in data.iterrows():
    city_map = folium.Map(location=[row['latitude'], row['longitude']], zoom_start=12)
    folium.Marker(
        location=[row['latitude'],row['longitude']],
        popup = f"{row['city']}: {row['accident_count']} accidents",
        icon = folium.Icon(color=get_marker_color(row['accident_count']))
    ).add_to(city_map)
    
    city_map.save(f"{row['city']}_accident_map.html")