#
# This code obtains all groups of which Frank is a member,
# by sending an HTTP request to the Spark server
# This is really everyone, because we will go through pages
#

import requests
import json
from pprint import pprint
import os

# A class that represents a single person
class Person(object):
  name = ""
  email = ""
# end of Person class

# A class that contains a message
class Message(object):
  text = "" # content of message
# end of Message class

# Let's make a class that represents a single rooms
class Room(object):
  name = ""
  isPerson = False
  id = ""

  # fills [message_list] with messages
  @staticmethod
  def GetMessages(bearId, roomId):
    url = "https://api.ciscospark.com/v1/messages"
    aut = "Bearer " + str(bearId)
    con = "application/json; charset=utf-8"
    header = {"Authorization":aut, "Content-type":con}
    query_params = {"roomId":roomId}
    runAgain = True
    runCounter = 0
    message_list = []

    while runAgain == True:
      runCounter = runCounter + 1
      if runCounter == 1:
        r = requests.get(url, headers=header, params=query_params)
      else:
        r = requests.get(url, headers=header)
      rjson = r.json( )
      #pprint(rjson)

      for msg in rjson["items"]:
        temp = Message( )
        if "text" in msg:
          temp.text = msg["text"]
          message_list.append(temp)

      print("Tot messages = " + str(len(message_list)))

      if "link" in r.headers:
        print("link in header")
        link = r.headers["link"]
        print("link = " + link)
        link = link.split(';', 1)[0]
        print("link = " + link)
        link = link[1:-1]
        print("link = " + link)
        runAgain = True
        url = link
      else:
        print("link NOT in header")
        runAgain = False

      if runCounter > 50: # too many, something is wrong
        runAgain = False
    return message_list
# end of Room class



def GetRoomOccupants(bearId, roomId):
  url = "https://api.ciscospark.com/v1/memberships"
  aut = "Bearer " + str(bearId)
  con = "application/json; charset=utf-8"
  header = {"Authorization":aut, "Content-type":con}
  query_params = {"roomId":roomId}

  r = requests.get(url, headers=header, params=query_params)
  rjson = r.json( )
  person_list = [] # list of persons
  for person in rjson["items"]:
    temp = Person( )
    temp.name = person["personDisplayName"]
    temp.email = person["personEmail"]
    person_list.append(temp)

  return person_list

def GetOccupiedRooms(bearId):
  url = "https://api.ciscospark.com/v1/rooms"
  aut = "Bearer " + str(bearId)
  runAgain = True # until we had all rooms
  runCounter = 0 # in case we get in infinite loop
  room_list = [] # list of rooms

  while runAgain == True:
    runCounter = runCounter + 1
    print("Doing request #" + str(runCounter) + "...")
    r = requests.get(url, headers={"Authorization":aut})
    rjson = r.json( )

    for room in rjson["items"]:
      temp = Room( )
      temp.name = room["title"]
      temp.id = room["id"]
      if room["type"] == "direct":
        temp.isPerson = True
      room_list.append(temp)

    print("Tot num rooms = " + str(len(room_list)))

    if "link" in r.headers:
      print("link in header")
      link = r.headers["link"]
      print("link = " + link)
      link = link.split(';', 1)[0]
      print("link = " + link)
      link = link[1:-1]
      print("link = " + link)
      runAgain = True
      url = link
    else:
      print("link NOT in header")
      runAgain = False

    if runCounter > 50: # too many, something is wrong
      runAgain = False

  return room_list
