#server test

#simple socket server example using makefile
import socket


def start_server(host_address: str, host_port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind((host_address, host_port))
        srv.listen()

        print(f"ICS 32 simple server listening on IP: {host_address} and port {host_port}")
        connection, address = srv.accept()

        with connection: 
            print(f"Client connected from {address[0]}")

            send = connection.makefile("w")
            recv = connection.makefile("r")

            while True:
                rec_msg = recv.readline()[:-1]
                


                print(rec_msg)
                print(f"Message received from client: {rec_msg}")

                if not rec_msg:
                    break
                
                send.write(f"{address[0]} sent me " + rec_msg + "\r\n")
                send.flush()

            print("Client disconnected")


if __name__ == "__main__":
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    start_server('127.0.0.1', 8080)