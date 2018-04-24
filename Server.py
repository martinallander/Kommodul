import bluetooth
import time
import pickle
from Sensor_Data import Sensor_Data

#Device adress found using finddevice.py
ma_bd_addr = "98:5F:D3:35:FC:EA"

ir = range(0,64)

def open_rec_server(server_sock, port):
    server_sock.bind(("",port))

def listen_to_server(server_sock):
    server_sock.listen(1)

def rec_server_accept(server_sock):
    client_sock,address = server_sock.accept()
    print "Accepted connection from ",address
    return client_sock

def close_reciever(client_sock, server_sock):
    client_sock.close()
    server_sock.close()

def connect_to_server(sock, bd_addr, port):
	sock.connect((bd_addr, port))

def close_sender(sock):
	sock.close()

def main():
	send_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	server_sock_rec=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

	open_rec_server(server_sock_rec,5)
	commands = list()

	#connect_to_server(send_sock, ma_bd_addr, 6)
	listen_to_server(server_sock_rec)
	client_sock = rec_server_accept(server_sock_rec)
	i = 0
	while i < 1000:
		sd = Sensor_Data([i, i+1 , i+2], [1.0, 2.0, 3.0], ir, 10.0)
		client_sock.send(pickle.dumps(sd))
		#close_sender(send_sock)
		data = client_sock.recv(1024)
		commands.append(data)
		i += 1
	close_reciever(client_sock, server_sock_rec)
	print(commands)

main()

	
