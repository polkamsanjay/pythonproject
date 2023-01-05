import sys
import requests

mac_address = "44:38:39:ff:ef:57"

# Query MAC address lookup API
api_key = "at_ymgTVBIb5rgbbsTPFzq2gr7RiMFyJ"
url = f"https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}"
response = requests.get(url)

# Extract company name, Company address, cpuntry code from API response
if response.status_code != 200:
    print(f"Failed to retrieve information for MAC address {mac_address}")
    sys.exit(1)

response_json = response.json()
company_name = response_json["vendorDetails"]["companyName"]
print(f"Company name: {company_name}")
company_address = response_json["vendorDetails"]["companyAddress"]
print(f"Company address: {company_address}")
country_Code = response_json["vendorDetails"]["countryCode"]
print(f"country Code: {country_Code}")
