import socket 

# creating a socket
try :
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    print(f"Socket was created successfully!")
except socket.error as error :
    print(f"Socket creation failed with error : {error}")

port = 5000

# binding
soc.connect(('127.0.0.1', port))
print(f'Server responded with : {soc.recv(1024)}')
soc.close()
