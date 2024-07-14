Nash-NetGeoScanner

The provided code is designed to perform network scanning using nmap and retrieve the geographical location of an IP address using an external API. It consists of two main functions: sanitize_input and Nmap, along with a third functionality to get the location of an IP address.

The sanitize_input function takes an input string, removes leading and trailing whitespace, and replaces internal spaces with no space. This sanitization ensures that the input is in a suitable format for further processing, such as forming a valid URL or command string.

The Nmap function accepts a website link, sanitizes it using the sanitize_input function, and constructs an nmap command to scan the website. The nmap tool, used for network scanning, requires elevated permissions, which is why the command is prefixed with sudo. The command string is safely split into a list using shlex.split, making it suitable for execution via subprocess.run.

The get_location function is responsible for querying the IP geolocation service using the provided IP address and API key. It constructs a URL for the API request, and if the response is successful (HTTP status code 200), it extracts relevant data such as the IP, city, region, country, latitude, and longitude. This data is then returned in a dictionary format.

The main code block first prompts the user to enter a website link, which is then scanned using the Nmap function. It subsequently prompts the user for an IP address and uses a predefined API key to fetch the location information for the provided IP address using the get_location function. If the location data is successfully retrieved, it prints the IP address, city, region, country, latitude, and longitude.

It is important to note the security implications of running nmap with sudo based on user input, as it can be potentially dangerous and lead to arbitrary code execution if the input is not properly sanitized. Additionally, the API key should be kept secure and not hard-coded in the script; using environment variables or a secure vault is recommended. Ensure that the necessary dependencies, such as the requests library and nmap, are installed on the system.

In practical usage, the user would enter a website link when prompted (e.g., example.com) and then provide an IP address (e.g., 8.8.8.8). The script will scan the provided website and fetch the geographical location information for the provided IP address, printing out the relevant details. It is crucial to have the necessary permissions to run nmap and be aware of the legal and ethical implications of scanning networks and IP addresses that you do not own or have explicit permission to scan. This script serves as a basic example and may require enhancements for robust error handling and security practices.
