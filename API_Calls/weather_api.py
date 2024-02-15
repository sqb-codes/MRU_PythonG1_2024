import urllib.request as url
import json
from geopy import geocoders 

location = input("Enter city/state/country : ")
api_key = "83e01e3dce5d28839bb5a177cb51af12"
gn = geocoders.GeoNames("example")
lat = gn.geocode(location)[1][0]
lon = gn.geocode(location)[1][1]

path = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = url.urlopen(path)
data = json.load(response)
print(data["main"])