# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kelly Bach
# kbach3@uci.edu
# 18576745

import json
from collections import namedtuple
import time

# Namedtuple to hold the values retrieved from json messages.
# TODO: update this named tuple to use DSP protocol keys
DataTuple = namedtuple('DataTuple', ["response", "token"])

def extract_json(json_msg:str) -> DataTuple:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  '''
  try:
    json_obj = json.loads(json_msg)
    response = json_obj["response"]
    token = json_obj["response"]["token"]
    return token
  except json.JSONDecodeError:
    print("Json cannot be decoded.")
    return None

def json_data(cmd, username, password, user_token=None, post=None, bio=None):
  data = None
  if cmd == "join":
    data = json.dumps({"join": {"username": username,"password": password,"token":""}})
  elif cmd == "post":
    if not user_token:
      raise ValueError("No user token found.")
    data = json.dumps({"token": user_token, "post": {"entry": post,"timestamp": time.time()}})
  elif cmd == "bio":
    if not user_token:
      raise ValueError("No user token found.")
    data = json.dumps({"token": user_token, "bio": {"entry": bio,"timestamp": time.time()}})
  return data

