import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8000

    client.connect((server_ip, port))
    
    while True:
        msg = input("You: ")
        client.send(msg.encode("utf-8")[:1024])

        response = client.recv(1024)
        response = response.decode("utf-8")

        if (response.lower() == "close"):
            client.close()
            break
        

        print(f"Server: {response}")

    client.close()
    print("Connection to server closed")

run_client()