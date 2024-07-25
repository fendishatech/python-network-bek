''' Chat Room Connection - Client to Client '''
import threading
import socket 

HOST = "127.0.0.1"
PORT = 5000

# creating a socket
try :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    print(f"Socket was created successfully!")
except socket.error as error :
    print(f"Socket creation failed with error : {error}")

# binding
server.bind((HOST, PORT))
print(f'socket with host : {HOST}, is bound to port : {PORT}')

# listening
server.listen()
print(f'socket is listening')

clients = []
aliases = []


def broadcastMsg (message):
    for client in clients :
        client.send(message)

def handleClient(client):
    print("client is",client)
    while True:
        try:
            message = client.recv(1024)
            broadcastMsg(message)
        except :
            print("Error")
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcastMsg(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

# Main function
def receive ():
    while True:
        print(f'Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The Alias of this client is {alias}'.encode('utf-8'))
        broadcastMsg(f'{alias} has joined the chatroom'.encode('utf-8'))
        client.send('you are now connected'.encode('utf-8'))


        thread = threading.Thread(target=handleClient, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()