import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mensaje = str(input("Introduce tu mensaje: "))

s.connect((socket.gethostname(), 1234))

s.send((mensaje).encode())

print("Mensaje enviado")

recivido = s.recv(1024).decode()
print("Mensaje recivido del servidor: " + recivido)