import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#HOST = '10.0.0.186'
HOST = '10.0.0.212'
PORT = 1234
s.connect((HOST, PORT))
print(f"Connected to {HOST}")
#s.setblocking(False)
while True:
    try:
        path = input("Enter file path: ")
        while True:
            try:
                with open(path, "r") as file:
                    data = file.read()
                    file_name = path.split('\\')[-1]
                    break
            except FileNotFoundError as e:
                data = None
                print(e)
                break
            except PermissionError as e:
                data = None
                print(e)
                break
            except OSError as e:
                data = None
                print(e)
                break
        if data is None:
            print("No data sent")
        else:
            s.sendall(bytes(file_name, 'utf-8'))
            file_n_con = s.recv(1024).decode('utf-8')
            print(file_n_con)
            s.sendall(bytes(data, "utf-8"))
            print("Data sent\n")
            confirm = s.recv(1024)
            confirm = confirm.decode('utf-8')
            print(confirm)
    except ConnectionResetError:
        print("Host disconnected; data not sent")
        s.close()
        break
    except ConnectionAbortedError:
        print("Host aborted; data not sent")
        s.close()
        break
