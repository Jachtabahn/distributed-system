import netifaces
import socket
import threading
import time

endpoint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endpoint.bind(("0.0.0.0", 9999))

PROTO = netifaces.AF_INET   # We want only IPv4, for now at least

# Get list of network interfaces
ifaces = netifaces.interfaces()

# Get addresses for each interface
if_addrs = [(netifaces.ifaddresses(iface), iface) for iface in ifaces]

# Filter for only IPv4 addresses
if_inet_addrs = [(tup[0][PROTO], tup[1]) for tup in if_addrs if PROTO in tup[0]]

iface_addrs = [(s['addr'], tup[1]) for tup in if_inet_addrs for s in tup[0] if 'addr' in s]

sockname = endpoint.getsockname()
print("getsockname():", "{}:{}".format(*sockname))
local_port = sockname[1]
for (address, name) in iface_addrs:
  print("{}:".format(name), "{}:{}".format(address, local_port))

def receive():
  event = endpoint.recvfrom(1024)
  print("Message:", event[0].decode())
  print("Originator:", "{}:{}".format(*event[1]))
  print("----------------------------------")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:

  address_with_port = input("Enter endpoint: ")
  address, port_string = address_with_port.split(":")
  port = int(port_string)

  message = input("Enter data to send to that endpoint: ")

  many_times_text = input("Enter how many times to send that data: ")
  many_times = int(many_times_text)

  for _ in range(many_times):
    endpoint.sendto(message.encode(), (address, port))
    time.sleep(0.001)
