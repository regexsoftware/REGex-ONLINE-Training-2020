import matplotlib.pyplot as plt
import folium
from  geopy.geocoders import Nominatim
geolocator = Nominatim()
import pandas as pd

df =  pd.read_csv('farms.csv')

city = df["city"]
city_list = list(city)
state = df["state"]
states=list(state)
state_list = list(state)

address = [city_list[i] + " " + state_list[i] for i in range(0, len(city_list))] 

mapit = folium.Map(location=[20.5937, 78.9629], zoom_start=6 )

for i in  address:
	loc = geolocator.geocode(i)
	lat = loc.latitude 
	long = loc.longitude
	folium.Marker( location=[ lat, long ], fill_color='#43d9de', radius=8 ).add_to( mapit )
mapit.save( 'indiaa.html')

farm_info = {} 
	
for item in states: 
	if item in farm_info: 
		farm_info[item] += 1
	else: 
		farm_info[item] = 1

print(farm_info)
 
states = list(farm_info.keys()) 
farm_number = list(farm_info.values()) 
exp = []
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
for i in range(0, len(states)):
	exp.append(0)
explode = tuple(exp)
plt.pie(farm_number, labels=states, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Farms in different states of India")
plt.show()





