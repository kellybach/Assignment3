#client test

#Client simple example using makefile
import socket


def start_client(server_address: str, server_port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server_address, server_port))

        send = client.makefile("w")
        recv = client.makefile("r")

        print(f"ICS32 simple client connected to {server_address} on {server_port}")

        while True:
            msg = input("Enter message to send: ")
            send.write(msg + "\r\n")
            send.flush()

            srv_msg = recv.readline()[:-1]
            print("Response received from server: ", srv_msg)

if __name__ == "__main__":
    print("ICS simple socket client")
    print("Server configuration")
    srv_ip = input("Enter server IP address : ")
    srv_port = input("Enter server port: ")
    start_client(srv_ip, int(srv_port))

