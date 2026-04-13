# client.py — sends an HTTP request to the server container

import urllib.request
import time

# Wait a moment for the server container to finish starting up
# before we try to connect to it
time.sleep(2)

# "server" here is the hostname — Docker automatically resolves
# this name to the server container's IP address on the shared network
url = "http://server:8080"

print(f"[client] connecting to {url} ...")
response = urllib.request.urlopen(url)

# Read the response body and decode it from bytes to a string
body = response.read().decode()
print(f"[client] response: {body}")
