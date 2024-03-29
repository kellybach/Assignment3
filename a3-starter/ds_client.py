# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kelly Bach
# kbach3@uci.edu
# 18576745

# server 168.235.86.101
# port 3021
import socket
import ds_protocol
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
      user = {"join": {"username": username,"password": password,"token":""}}
      json_user = json.dumps(user)
      send.write(json_user + "\r\n")
      send.flush()
      srv_msg = recv.readline()[:-1]
      print("Response received from server: ", srv_msg)
      if "token" in str(srv_msg):
        token = ds_protocol.extract_json(str(srv_msg))
      if message:
        action = "post"
        data_msg = ds_protocol.json_data(action, username, password, token, post = message)
        send.write(data_msg + "\r\n")
        send.flush()
      if bio:
        action = "bio"
        data_msg = ds_protocol.json_data(action, username, password, token, bio = bio)
        send.write(data_msg + "\r\n")
        send.flush()
      srv_msg = recv.readline()[:-1]
      print("Response received from server: ", srv_msg)
      srv_msg = json.loads(srv_msg)
      if "response" in srv_msg:
        if srv_msg["response"]["type"] == "ok":
          return True
        else:
          error = srv_msg["response"]["message"]
          print("Error: ", error)
          return False
      print('done')
  except Exception as error:
    print("Error: ", error, 'lmao')
    return False