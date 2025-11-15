import socket

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 1234

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    while True:
        client, address = server.accept()
        print(f"Connection Estabished - {address[0]} : {address[1]}")

        string = client.recv(1024)
        string = string.decode('utf-8')
        string = string.upper() # mengubah string menjadi huruf besar semua meskipun yang diinput huruf kecil

        #1 
        # print(string) # hilangkan pagar nya agar kode bisa dipake (saran #1 dan #2 itu digunakan salah satu saja)

        #2
        client.send(bytes(string, 'utf-8')) # hilangkan pagar nya agar kode bisa dipake

        client.close()