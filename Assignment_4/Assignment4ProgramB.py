import socket
programB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
programB.connect(('127.0.0.1', 8080))
talk = programB.recv(1024).decode()
programB.send(talk.upper().encode())
print(talk)