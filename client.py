import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
data = bytes("HELLO", 'utf-8')
sock.sendto(data, ("127.0.0.1", 33333))
print("Client Sent : ", data)
data, address = sock.recvfrom(4096)
print("Client received : ", data.decode('utf-8'))
sock.close()