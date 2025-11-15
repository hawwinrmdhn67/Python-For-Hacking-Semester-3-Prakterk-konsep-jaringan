import socket

targetHost = "127.0.0.1"
targetPort = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP

#kirim data
client.sendto(b"Hai Saya Hawwin Ramadhan", (targetHost, targetPort))

#menerima data
data, addr = client.recvfrom(4096)
print ("pesan dari server: \"{}\"".format(data.decode()))

client.close()