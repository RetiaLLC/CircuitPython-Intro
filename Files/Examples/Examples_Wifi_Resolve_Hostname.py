# 2023 by Skickar for Retia LLC
import socketpool
import wifi

# Connect to a Wi-Fi network
ssid = input("Enter SSID: ")
password = input("Enter password: ")
wifi.radio.connect(ssid, password)

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Resolve a hostname
hostname = input("Enter hostname: ")
addr_info = pool.getaddrinfo(hostname, 0, pool.AF_INET, pool.SOCK_STREAM)
ip_address = addr_info[0][4][0]
print(f"{hostname} resolved to {ip_address}")
