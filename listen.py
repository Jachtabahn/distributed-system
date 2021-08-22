import socket
import struct

# Initialise socket for IPv6 datagrams
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allows address to be reused
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binds to all interfaces on the given port
sock.bind(('', 8080))

# Allow messages from this socket to loop back for development
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)

data, addr = sock.recvfrom(1024)

print("data, addr")
print(data, addr)
