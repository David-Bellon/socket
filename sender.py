import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except:
    print("ERRO with socket")

port = 12345

s.connect(("127.0.0.1", port))

message = str(input("Introduce el mensaje a enviar: "))
s.send(message.encode())
    
