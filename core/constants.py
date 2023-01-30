import socket


"""
documentation: https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
"""

HOST = ''
IP = '192.168.10.1'
PORT = 8889
SERVER = "0.0.0.0"
LOCAL_ADDRESS = (HOST, PORT)


udp_socket = socket.socket(socket.AF_INET, socket.AF_INET)


def test_server_socket() -> None:
    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = LOCAL_ADDRESS
    server_socket.bind(server_address)

    print(f'Starting up on {server_address}:{server_address}')

    # Receive data from the client
    while True:
        data, client_address = server_socket.recvfrom(4096)
        print('Received {} bytes from {}'.format(len(data), client_address))


def test_client_socket() -> None:

    # Create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the timeout for the socket
    client_socket.settimeout(1.0)

    # Send data to the server
    server_address = (IP, PORT)
    message = b'Hello, server!'
    client_socket.sendto(message, server_address)

    # Receive data from the server
    try:
        data, server_address = client_socket.recvfrom(4096)
        print('Received {} bytes from {}'.format(len(data), server_address))
    except socket.timeout:
        print('Timed out waiting for a response from the server')


def test_connection() -> None:
    tello_address = (IP, PORT)
    udp_socket.bind(LOCAL_ADDRESS)


def test_receive() -> None:
    count = 0
    while True:
        try:
            i, server = udp_socket.recvfrom(1518)
            print(i.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break


def main() -> None:
    test_client_socket()
    test_server_socket()
    test_connection()
    test_receive()


if __name__ == "__main__":
    main()
