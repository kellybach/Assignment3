# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kelly Bach
# kbach3@uci.edu
# 18576745

# server 168.235.86.101
# port 3021
import socket
import json
def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  try: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))
      send = client.makefile("w")
      recv = client.makefile("r")
      user = '{"join": {"username": username,"password": password,"token":""}}'
      print(user)
      send.write(user + "\n\r")
      send.flush()
  except:
    pass
      
  return 


def test(server = '192.168.100.5', port = 7777, username = 'blah', password = 'www' ):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))
      send = client.makefile("w")
      recv = client.makefile("r")
      user = '{"join": {"username": username,"password": password,"token":""}}'
      print(user)
      send.write(user + "\r\n")
      send.flush()

test()  
"""
#serverinfo.send.write(whattowrite + '\r\n')
serverinfo.send.flush()

to read 
#cmd=serverconnection.recv.readline()[:-1]
#return cmd

server info is client

    def talk():
      send = client.makefile("w")
      msg = input("Enter message to send: ")
      send.write(msg + "\r\n")
      send.flush()

    def receive():
      recv = client.makefile("r")
      srv_msg = recv.readline()[:-1]
      print("Response received from server: ", srv_msg)

    print("ICS32 simple client connected to "+
    f"{server} on {port}")
"""