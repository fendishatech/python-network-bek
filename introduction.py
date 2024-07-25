''' Socket Programming with pyhton '''

import socket
import sys

# get an ip of a website with python
# ip = socket.gethostbyname("www.github.com")
# print(ip)

# creating a socket
try :
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    print(f"Socket was created successfully!")
except socket.error as error :
    print(f"Socket creation failed with error : {error}")

port = 80
host_name = "www.github.com" 
try :
    host_ip = socket.gethostbyname(host_name)
except socket.gaierror:
    print("There was an error connecting to host")
    sys.exit()

soc.connect((host_ip,port))
print(f"Socket created successfully to host : {host_name} with ip : {host_ip} on port : {port}")