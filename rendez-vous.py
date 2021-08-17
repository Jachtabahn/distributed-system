import socket

endpoint = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

endpoint.bind(("0.0.0.0", 8888))
while True:
  event = endpoint.recvfrom(1024)
  print("Message:", event[0].decode())
  print("Originator:", "{}:{}".format(*event[1]))
  print("----------------------------------")
