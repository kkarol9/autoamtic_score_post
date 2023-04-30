import requests
import json

url = "https://api.sofascore.com/api/v1/sport/tennis/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua-mobile": "?1",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers)

# Sprawdzenie, czy pobranie danych się powiodło
if response.status_code != 200:
    print(f"Błąd pobierania danych, kod statusu: {response.status_code}")
else:
    # Zapisanie danych do pliku JSON
    with open("tenis.json", "w") as f:
        json.dump(response.json(), f)