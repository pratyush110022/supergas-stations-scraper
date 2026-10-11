import requests
import pandas as pd
import time

URL = "https://www.supergas.com/api/dealer/searchbyarea"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/json; charset=UTF-8",
    "Origin": "https://www.supergas.com",
    "Referer": "https://www.supergas.com/franchisee-locator?view=map&dealerType=Autogas"
}

records = {}

# Grid covering India
latitudes = [8, 11, 14, 17, 20, 23, 26, 29, 32]
longitudes = [69, 72, 75, 78, 81, 84, 87, 90, 93]

for lat in latitudes:
    for lng in longitudes:

        print(f"Searching {lat}, {lng}")

        payload = {
            "dealerBrandNames": [],
            "dealerStoreTypes": [],
            "dealerType": "Autogas",
            "filters": [],
            "hasSpecialOrderAvailable": False,
            "isBio": False,
            "isDeliveryAvailable": False,
            "isMobile": True,
            "isOpenNow": False,
            "isPreferredPartner": False,
            "isTruckLpg": False,
            "sortBy": "Distance",
            "tags": [],
            "zoomLevel": 7,

            "location": {
                "lat": lat,
                "lng": lng
            },

            "northEast": {
                "lat": lat + 3,
                "lng": lng + 3
            },

            "southWest": {
                "lat": lat - 3,
                "lng": lng - 3
            }
        }

        try:
            r = requests.post(URL, headers=HEADERS, json=payload, timeout=60)

            data = r.json()

            dealers = data.get("Dealers", [])

            print("Found:", len(dealers))

            for d in dealers:

                loc = d.get("geometry", {}).get("location", {})

                row = {
                    "ID": d.get("id"),
                    "Station Name": d.get("description"),
                    "Latitude": loc.get("lat"),
                    "Longitude": loc.get("lng"),
                    "Phone": ", ".join(d.get("dealerPhones", [])),
                    "Email": d.get("email"),
                    "Website": d.get("websiteUrl"),
                    "Store Type": d.get("storeType"),
                    "Preferred": d.get("isPreferredPartner"),
                    "Delivery": d.get("isDeliveryAvailable"),
                    "Bio": d.get("isBio"),
                    "Icon": d.get("icon")
                }

                records[d["id"]] = row

        except Exception as e:
            print(e)

        time.sleep(0.5)

df = pd.DataFrame(records.values())

df.sort_values("Station Name", inplace=True)

df.to_excel("SUPERGAS_All_Stations.xlsx", index=False)

print()
print("Total Unique Stations:", len(df))
print("Saved: SUPERGAS_All_Stations.xlsx")