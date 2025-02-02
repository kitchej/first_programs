import socket
from datetime import datetime
import selectors

sel = selectors.DefaultSelector()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST = '10.0.0.214'
    PORT = 10000
    s.bind((HOST, PORT))

    while True:
        s.listen()
        print("Listening...")
        sel.register(s, selectors.EVENT_READ, data=None)
        connection, address = s.accept()
        print(f"Connection established with {address}")
        while True:
            try:
                client_msg = connection.recv(1024)
                if not client_msg:
                    print("Client disconnected")
                    break
                client_msg = client_msg.decode('utf-8')
                log_entry = f"Received: {datetime.now()} | Message: {client_msg}\n"
                print(log_entry)
                with open(r"C:\Users\Josh\Desktop\received_text.txt", 'a+') as file:
                    file.write(log_entry)
            except ConnectionResetError:
                print("Client disconnected")
                break
            except ConnectionAbortedError:
                print("Connection Aborted")
                break
            except OSError:
                break


        """while True:
            msg = input("Enter a message: ")
            try:
                connection.send(bytes(program, "utf-8"))
                print("Message sent\n")
            except ConnectionResetError:
                print("Client disconnected")
                break
            except ConnectionAbortedError:
                print("Connection Aborted")
                break
"""