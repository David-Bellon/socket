import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Conexion de ", addr)
    recivido = c.recv(1024).decode()
    print(recivido)
    if recivido == "hola":
        c.send('Adios'.encode())
    elif recivido == "adios":
        c.send("servidor cerrado".encode())
        break
    else:
        c.send(b'Un hola no costaba')
    c.close()