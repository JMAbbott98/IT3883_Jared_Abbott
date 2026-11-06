	# Program Name: Assignment4.py (use the name the program is saved as)
	# Course: IT3883/Section W01
	# Student Name: Jared Abbott
	# Assignment Number: Lab4
	# Due Date: 11/01/ 2026
	# Purpose: The purpose of this program is to get program A to talk to Program B. Program B will also respond and talk back to program A
	# List: https://www.youtube.com/watch?v=bwTAVGg_kVs
    # https://www.youtube.com/watch?v=BlQbUV_W954&list=PLS1QulWo1RIZGSgRsn0b8w9uoWM1gHDpo&index=13
    # https://www.youtube.com/watch?v=I5P3hqdyc2g&list=PLS1QulWo1RIZGSgRsn0b8w9uoWM1gHDpo&index=8

import socket
programA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
programA.bind(('localhost', 8080))
programA.listen(5)
userInput = input("Enter a string: ")
while True:
    programB, addr = programA.accept()
    programB.send(userInput.encode())
    print(programB.recv(1024).decode())
    break

