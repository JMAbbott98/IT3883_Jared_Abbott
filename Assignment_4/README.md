# Program Name: Assignment4.py (use the name the program is saved as)
	# Course: IT3883/Section W01
	# Student Name: Jared Abbott
	# Assignment Number: Lab4
	# Due Date: 11/01/ 2026
	# Purpose: The purpose of this program is to get program A to talk to Program B. Program B will also respond and talk back to program A
	# List:
import socket
programA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
programA.bind(('localhost', 8080))
programA.listen(5)
userInput = input("Enter a string: ")
while True:
    programB, addr = programA.accept()
    programB.send(userInput.encode())
    print(programB.recv(1024).decode())

import socket
programB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
programB.connect(('127.0.0.1', 8080))
talk = programB.recv(1024).decode()
programB.send(talk.upper().encode())
print(talk)

<img width="1920" height="1080" alt="ProgramAOutput" src="https://github.com/user-attachments/assets/af6d5f69-fb78-4973-a549-49b41e2cccea" />
<img width="1920" height="1080" alt="ProgramBOutput" src="https://github.com/user-attachments/assets/6dc2cfbc-e153-49b1-8373-51c28b7df26e" />
