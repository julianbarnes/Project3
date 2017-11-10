from socket import *
import sys
import io
import argparse
import os



if len(sys.argv) <= 1:
	print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
	sys.exit(2)
	
# Create a server socket, bind it to a port and start listening

def main():
	#Request params from user
	args = get_params()
	#Initialize socket 
	server_socket = socket(AF_INET, SOCK_STREAM)
	server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	#Bind socket to port 
	server_socket.bind(('',args.port))
	#Set socket to listen for connection requests
	server_socket.listen(10)
	
	while True:
		# Strat receiving data from the client
		print('Ready to serve...')
		tcpCliSock, addr = tcpSerSock.accept()
		connect_client(tcpCliSock, args)
	server_socket.close()
	sys.exit()
		
def get_params():
	#Initialize parser
	parser = argparse.ArgumentParser(description='Configure IP Address and Port number for server.')
	parser.add_argument('port', type=int, help='Port number')
	parser.add_argument('root', type=str, help='Root folder')
	
	#Set variable args to results of parser
	args = parser.parse_args()
	return args

def connect_client(connection, args):
	print('Received a connection from:', addr)
		message = connection.recv(1024)
		print(message)
		# Extract the filename from the given message
		print(message.split()[1])
		filename = message.split()[1].partition("/")[2]
		print(filename)
		fileExist = "false"
		filetouse = "/" + filename
		print(filetouse)
		try:
			# Check wether the file exist in the cache
			f = open(filetouse[1:], "rb")                      
			outputdata = f.read()                        
			fileExist = "true"
			# ProxyServer finds a cache hit and generates a response message
			connection.send("HTTP/1.0 200 OK\r\n")            
			connection.send("Content-Type:text/html\r\n")
			connection.send(outputdata)
			
			print('Read from cache')   
		# Error handling for file not found in cache
		except IOError:
			if fileExist == "false": 
				# Create a socket on the proxyserver
				c = # Fill in start.		# Fill in end.
				hostn = filename.replace("www.","",1)         
				print(hostn)                                  
				try:
					# Connect to the socket to port 80
					# Fill in start.		
					# Fill in end.
					# Create a temporary file on this socket and ask port 80 for the file requested by the client
					fileobj = c.makefile('r', 0)               
					fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")  
					# Read the response into buffer
					# Fill in start.		
					# Fill in end.
					# Create a new file in the cache for the requested file. 
					# Also send the response in the buffer to client socket and the corresponding file in the cache
					tmpFile = open("./" + filename,"wb")  
					# Fill in start.		
					# Fill in end.			
				except:
					print("Illegal request")                                               
			else:
				# HTTP response message for file not found
				# Fill in start.		
				# Fill in end.
		# Close the client and the server sockets    
		tcpCliSock.close() 
	# Fill in start.		
	# Fill in end.