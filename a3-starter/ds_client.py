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
      print(srv_msg)
      srv_response = json.loads(srv_msg)
      print(srv_response)
      if "token" in str(srv_msg):
        token = ds_protocol.extract_json(str(srv_msg))
        print('yay')
      if message:
        pass
        """
        action = "post"
        data_msg = ds_protocol.json_data(action, username, password, token, post = message)
        send.write(data_msg + "\r\n")
        send.flush()
        """
      else:
        pass
      if bio:
        pass
      else: 
        pass
      srv_msg = recv.readline()[:-1]
      print("Response received from server: ", srv_msg)
      srv_response = json.loads(srv_msg)
      if "response" in srv_response:
        if srv_response["response"]["type"] == "ok":
          return True
        else:
          error = srv_response["response"]["message"]
          print("Error: ", error)
          return False
  except Exception as error:
    print("Error: ", error)
    return False

send('168.235.86.101', 3021, 'meow', 'meow','meow','meow')
#send('127.0.0.1', 8080, 'test', 'meow','meow','meow')