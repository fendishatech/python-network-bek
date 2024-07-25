import socket 

# creating a socket
try :
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    print(f"Socket was created successfully!")
except socket.error as error :
    print(f"Socket creation failed with error : {error}")

port = 5000

# binding
soc.bind(('', port))
print(f'socket bound to port : {port}')

# listening
soc.listen(5)
print(f'socket is listening')

# server loop
while True:
    c,addr = soc.accept()
    print(f'Got Connection from : {addr}')
    message = ("Response for connecting")
    c.send(message.encode())
    c.close()