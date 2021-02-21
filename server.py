import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = os.getenv('port', 33333)

server = (server_address, server_port)
sock.bind(server)
print('Listening on ' + server_address + ':' + str(server_port))

try:
    while True:
        payload, client_address = sock.recvfrom(1024)
        print('Echoing data back to ' + str(client_address))
        sent = sock.sendto(payload, client_address)
except KeyboardInterrupt:
    print('KeyboardInterrupt')
    sock.shutdown
    sock.close()
