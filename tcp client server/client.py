import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port)) 
    
    #1 (Pake keduanya jangan di kasi pagar)
    string = input("Enter string: ")
    server.send(bytes(string, 'utf-8'))

    #2
    buffer = server.recv(1024)
    buffer = buffer.decode('utf-8')
    print(f"Server: {buffer}")