import requests

API_key = "27be317712d2e0375eddb213e8dc4cf2fbbbb05662302b9b819757b6f9cb4e8b"

bitcoin = float(input("How many bitcoins do you want to buy?: "))

response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + API_key)

bitcoin_price = float(response.json()["data"]["priceUsd"]) 

total = round(bitcoin * bitcoin_price, 2)
print(f"Your total will be: ${total}")