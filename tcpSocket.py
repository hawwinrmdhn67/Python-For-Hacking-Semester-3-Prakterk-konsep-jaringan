import socket 

targetHost = "www.google.com"
targetport = 80

#membuat socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetport))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#menangkap respon
response = client.recv(4096)   
print(response.decode())

client.close()