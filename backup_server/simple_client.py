import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST = '10.0.0.214'
    PORT = 10000
    s.connect((HOST, PORT))
    print(f"Connected to {HOST}")
    while True:
        msg = input("Enter a message: ")
        try:
            s.send(bytes(msg, "utf-8"))
            print("Message sent\n")
        except ConnectionResetError:
            print("Server disconnected")
            break
        except ConnectionAbortedError:
            print("Connection Aborted")
            break
