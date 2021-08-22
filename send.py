import socket
import struct

# Create ipv6 datagram socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# Allow own messages to be sent back (for local testing)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)

message = "hello world"
sock.sendto(message.encode('utf-8'), ("fe80::82fe:9d1b:cca7:c0ef", 8080))
print("SENT:", message)
