import json
import requests
import socket

endpoint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

  message = input("Collect from server now?")
  ips_text = requests.get("http://157.245.241.77:8888").text
  ips = json.loads(ips_text)["ips"]
  print(ips)
  for ip in ips:
    print("We've got the IP:", ip)
  receiver_ip = ips[1]

  address_with_port = input("Enter address of server: ")
  address, port_string = address_with_port.split(":")
  port = int(port_string)

  message = input("Enter data to send to server: ")
  res = endpoint.sendto(message.encode(), (address, port))
  print("res:", res)
