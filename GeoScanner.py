import requests
import subprocess
import shlex

def sanitize_input(input_string):
    return input_string.strip().replace(" ", "")

def Nmap(website_link):
    print("Eg: example.com")
    safe_link = sanitize_input(website_link)
    command = f"sudo nmap {safe_link} -sS"
    subprocess.run(shlex.split(command))

def get_location(ip, api_key):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("state_prov"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude")
        }
    else:
        return None

Link = input("Enter website link ")
Nmap(Link)
ip_address = input("Enter IP address : ")
api_key = input("Enter API key : ")
location = get_location(ip_address, api_key)
if location:
    print(f"IP: {location['ip']}")
    print(f"City: {location['city']}")
    print(f"Region: {location['region']}")
    print(f"Country: {location['country']}")
    print(f"Latitude: {location['latitude']}")
    print(f"Longitude: {location['longitude']}")
else:
    print("Failed to get location data.")

