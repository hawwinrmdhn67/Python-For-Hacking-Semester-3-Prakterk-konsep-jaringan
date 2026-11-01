# 🐍 Python TCP & UDP Client–Server

Project ini merupakan implementasi sederhana komunikasi jaringan menggunakan protokol **TCP** dan **UDP** dengan bahasa pemrograman Python.
Cocok untuk pembelajaran **networking**, **ethical hacking**, dan **dasar penetration testing legal**.

---

## 📁 Struktur Project

```
tcp client server/
│── client.py        # Client TCP
│── server.py        # Server TCP
│── tcpSocket.py     # Modul socket TCP (versi modular)
│── udpServer.py     # Server UDP
│── udpSocket.py     # Client/Socket UDP
│── readme.md        # Dokumentasi project
```

---

## 🚀 Cara Menjalankan

### **1. Menjalankan TCP Server**

```bash
cd "tcp client server"
python server.py
```

### **Outputnya**

<img width="683" height="117" alt="image" src="https://github.com/user-attachments/assets/cdd20543-2d6d-44bf-be66-07dba456d6d0" />

### **Output setelah menjalankan client.py**

<img width="673" height="136" alt="image" src="https://github.com/user-attachments/assets/c1027b6c-2b41-4b20-a6cc-9587bdd1556c" />


### **2. Menjalankan TCP Client**

```bash
cd "tcp client server"
python client.py
```

### **Outputnya**

<img width="676" height="184" alt="image" src="https://github.com/user-attachments/assets/c3b515b2-2ce4-4bec-920c-983e5f489ce6" />

---

### **3. Menjalankan UDP Server**

```bash
python udpServer.py
```

### **Outputnya**

<img width="563" height="90" alt="image" src="https://github.com/user-attachments/assets/7f4ef6b6-eee0-468a-91ca-0bc4adfc97b4" />

### **Output setelah menjalankan udpSocket.py**

<img width="546" height="129" alt="image" src="https://github.com/user-attachments/assets/a8dbfec9-1ea6-467b-a712-2dbcee693969" />


### **4. Menjalankan UDP Client**

```bash
python udpSocket.py
```

### **Outputnya**

<img width="561" height="140" alt="image" src="https://github.com/user-attachments/assets/5b61138e-72b4-48af-8ff4-3e22cf7fcf6c" />

---

## 📡 Penjelasan Singkat Cara Kerja

### **TCP (Transmission Control Protocol)**

* Bersifat **connection-oriented**
* Melakukan *3-way handshake* sebelum mengirim data
* Menjamin data sampai dengan urutan yang benar
* Cocok untuk aplikasi: chat, transfer file, login system

### **UDP (User Datagram Protocol)**

* Bersifat **connectionless**
* Tidak menjamin data terkirim
* Lebih cepat, latency rendah
* Cocok untuk: streaming, game online, sensor data

---

## 🧩 Detail File

### **server.py**

Server TCP yang:

* Bind ke IP dan port
* Menunggu koneksi
* Menerima data dari client
* Mengirim response balik

### **client.py**

Client TCP yang:

* Terhubung ke server
* Mengirim pesan
* Menerima balasan

### **tcpSocket.py**

Modul socket TCP untuk:

* Modularisasi
* Reusable kode program
  Cocok kalau ingin menambahkan fitur sendiri.

### **udpServer.py**

Server UDP yang menerima packet tanpa koneksi.

### **udpSocket.py**

Client UDP yang bisa mengirim data ke server tanpa handshake.

---

## 📘 Requirements

* Python 3.8 atau lebih baru
* Tidak butuh library tambahan
  Menggunakan built-in module:

```python
import socket
```

---
