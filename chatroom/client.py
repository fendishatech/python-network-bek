import threading
import socket

HOST= "127.0.0.1"
PORT= 5000


alias = input("Choose an alias >>>")


# creating a client socket
try :
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    print(f"Client socket was created successfully!")
except socket.error as error :
    print(f"Client socket creation failed with error : {error}")

# conn
client.connect((HOST, PORT))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "alias?" :
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("Error receiving message")
            client.close()
            break

def client_send():
    while True:
        try:
            message = f'{alias} : {input('')}'

            client.send(message.encode('utf-8'))
        except:
            print("Error sending message")
            client.close()
            break


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()


