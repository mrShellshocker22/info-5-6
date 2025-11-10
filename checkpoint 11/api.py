import requests
import json

song = input("What song do you want?: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + song)
#print(json.dumps(response.json(), indent=2 ))

search = response.json()
for result in search['results']:
    print(result["trackName"], result["artistName"])

city = input("City: ")
response2 = requests.get("http://goweather.xyz/weather/" + city)
print(response2.json())