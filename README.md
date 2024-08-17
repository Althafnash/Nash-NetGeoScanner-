# Nash-NetGeoScanner

**Nash-NetGeoScanner** is a Python-based tool that combines network scanning using nmap with IP geolocation retrieval. It allows you to scan networks and obtain geographical information about IP addresses.

## Features

- **Network Scanning:** Perform network scans using nmap. The tool scans a given website link for open ports and other network-related information.
- **IP Geolocation:** Retrieve the geographical location of an IP address using an external API. The tool returns information such as city, region, country, latitude, and longitude.

## Functions

- **sanitize_input:** Cleans and formats the input string to ensure it is in a suitable format for further processing.
- **Nmap:** Scans a website link after sanitizing it, using nmap to gather network information.
- **get_location:** Queries an external API to retrieve geographical data for a given IP address.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Nash-NetGeoScanner.git
   python nash_netgeoscanner.py

Enter the website link and IP address when prompted to perform the scan and retrieve location data.

## Important Notes

Security: Running nmap with elevated permissions (sudo) based on user input can be potentially dangerous. Ensure proper input sanitization and only scan networks/IP addresses you have permission to scan.
API Key Management: Keep your API key secure. Avoid hard-coding it in the script; use environment variables or a secure vault instead.
