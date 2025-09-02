import requests

url = f"https://api.aladhan.com/v1/timingsByCity/30-08-2025?city=Jakarta&country=Indonesia&method=20"

response = requests.get(url) # Http Get (ambil data)

data_json = response.json()

print("JADWAL SHOLAT - JSON API")

print("-" * 40)

print(data_json)

jadwal_sholat = data_json['data']['timings']
print(f"-> Shubuh = {jadwal_sholat['fajr']}")
print(f"-> Maghrib = {jadwal_sholat['maghrib']}")
print(f"-> Dzuhur = {jadwal_sholat['dzuhr']}")