from socket import *
import sys
import io
import argparse
import os
import string
import thread
	
# Create a server socket, bind it to a port and start listening
def main():
	#Request params from user
	args = get_params()
	try:
		#Initialize socket 
		global client_proxy
		client_proxy = socket(AF_INET, SOCK_STREAM)
		client_proxy.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		#Bind socket to port 
		client_proxy.bind(('',args.port))
		#Set socket to listen for connection requests
		client_proxy.listen(10)
	except Exception, e:
		print(e)


	while True:
		#Start receiving data from the client
		print('Starting proxy server on port ' + str(args.port))
		global proxy_client
		proxy_client = client_proxy.accept()[0]
		request = proxy_client.recv(1024)
		request = remove_hopper(request)
		print(request)

		lines = request.split("\n")
		#print(lines)
		hostandport = lines[1].split(":")
		host = lines[1][6:]
		if(len(hostandport) > 2):
			port = int(hostandport[2])
		else:
			port = 80

		#print("PORT IS " + str(port) + "\n")
		#print("HOST IS " + host + str(len(host)))

		#print("After parse")
		#print(lines)

		thread.start_new_thread(request_server, (host, port, request, ))
		#request_server(host, port, request)
		#filename = request.split()[1].partition("/")[2]
		#print("filename: " + filename)
		#print(request)
		#connect_client(proxy_client, args)
	client_proxy.close()
	sys.exit()
	
			
		
def get_params():
	#Initialize parser
	parser = argparse.ArgumentParser(description='Configure IP Address and Port number for server.')
	parser.add_argument('port', type=int, help='Port number')
	
	#Set variable args to results of parser
	args = parser.parse_args()
	return args

def request_server(host, port, request):
	try:
		send_socket = socket(AF_INET, SOCK_STREAM)                                  
		#Connect to the socket to port 80 (Internet)
		send_socket.connect(('cs.yonsei.ac.kr', port))
		#print(request)
		send_socket.send(request)
		while True:
			response = send_socket.recv(1024)
			if(len(response) > 0):
				#response = remove_hopper(response)
				parsed_response = remove_hopper(response) 
				#print(response)
				proxy_client.send(response)
			else:
				break
		proxy_client.close()

	except Exception as e:
		proxy_client.close()
		print(e)

def remove_hopper(message):
	lines = message.split("\n")
	hoptohop = ["Connection", "Transfer-Encoding", "Keep-Alive", "Proxy-Authorization", "Proxy-Authentication", "Trailer", "Upgrade"]
	output = ""
	#print(request)
	for line in lines:
		if(line.split(":")[0] not in hoptohop):
			output = output + line + "\n"
	return output
	
	
main()


