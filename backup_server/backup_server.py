import socket
import os

"""DOES NOT WORK AT THE MOMENT"""

while True:
    path = input("Enter path to save data to: ")
    try:
        os.chdir(path)
        break
    except PermissionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)
    except TypeError as e:
        print(e)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '10.0.0.214'
PORT = 1234
s.bind((HOST, PORT))
while True:
    s.listen(5)
    print("Listening...")
    connection, address = s.accept()
    print(f"Connection established with {address}")
    while True:
        try:
            file_name = connection.recv(1024000)
            client_data = connection.recv(1024000)
            file_name = file_name.decode('utf-8')
            client_data = client_data.decode('utf-8')
            try:
                with open(file_name, "w+") as back_up:
                    back_up.write(client_data)
                    connection.send(bytes("Message from server: Data received and saved!", 'utf-8'))
                    print("Data recived from client")
            except OSError as e:
                connection.send(bytes("Message from server: Error - data NOT saved", 'utf-8'))
                print(e)
                break
        except ConnectionResetError:
            print("Client disconnected")
            break
        except ConnectionAbortedError:
            print("Client aborted")
            break
