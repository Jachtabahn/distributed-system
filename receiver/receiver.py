import netifaces
import requests
import socket

PROTO = netifaces.AF_INET   # We want only IPv4, for now at least

# Get list of network interfaces
ifaces = netifaces.interfaces()

# Get addresses for each interface
if_addrs = [(netifaces.ifaddresses(iface), iface) for iface in ifaces]

# Filter for only IPv4 addresses
if_inet_addrs = [(tup[0][PROTO], tup[1]) for tup in if_addrs if PROTO in tup[0]]

iface_addrs = [(s['addr'], tup[1]) for tup in if_inet_addrs for s in tup[0] if 'addr' in s]

url = "http://157.245.241.77:8888"

for (address, name) in iface_addrs:
  print("url + \": \" address", url + ": " + address)
  response = requests.post(url, data = address + ":8888")

endpoint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

endpoint.bind(("0.0.0.0", 8888))
while True:
  print("endpoint.recvfrom(1024):", endpoint.recvfrom(1024))
