import socket

s = socket.socket()

port = 12345

s.bind(("", port))

s.listen(5)

while(True):
    c, addr = s.accept()
    print("Connection from", addr)
    data_recived = c.recv(1024)

    if not data_recived:
        c.sendall("No has mandado nada. Cerrando conexion")
        break
    else:
        print(data_recived)
        