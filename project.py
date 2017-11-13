from socket import *
import sys
import io
import argparse
import os
	
# Create a server socket, bind it to a port and start listening
def main():
	#Request params from user
	args = get_params()
	#Initialize socket 
	global client_proxy
	client_proxy = socket(AF_INET, SOCK_STREAM)
	client_proxy.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	#Bind socket to port 
	client_proxy.bind(('',args.port))
	#Set socket to listen for connection requests
	client_proxy.listen(10)
	print(str(args.port) + " " + str(args.root))
	
	while True:
		#Start receiving data from the client
		print('Ready to serve...')
		global proxy_client
		proxy_client = client_proxy.accept()[0]
		request = proxy_client.recv(1024)
		request_server(request)
		print(request)
		#connect_client(proxy_client, args)
	client_proxy.close()
	sys.exit()
		
def get_params():
	#Initialize parser
	parser = argparse.ArgumentParser(description='Configure IP Address and Port number for server.')
	parser.add_argument('port', type=int, help='Port number')
	parser.add_argument('root', type=str, help='Root folder')
	
	#Set variable args to results of parser
	args = parser.parse_args()
	return args

def request_server(request):
	send_socket = socket()                                  
	try:
		#Connect to the socket to port 12000
		send_socket.connect(('',12000))
		send_socket.send(request)
		response = send_socket.recv(1024)
		proxy_client.send(response)
		
	except:
		print("Could not connect to server")
	
main()


