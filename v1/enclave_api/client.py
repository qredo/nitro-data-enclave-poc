import sys
import socket
import requests
import json


def main():

    # Create a vsock socket object
    s = socket.socket(socket.AF_VSOCK, socket.SOCK_STREAM)

    # Get CID from command line parameter
    cid = int(sys.argv[1])

    # The port should match the server running in enclave
    port = 5000

    # Connect to the server
    s.connect((cid, port))

    # send query to server running in enclave
    package = {"hostname":"binance.com","port":443}
    s.send(str.encode(json.dumps(package)))
    print(s.recv(16384).decode())

    # close the connection
    s.close()

if __name__ == '__main__':
    main()
