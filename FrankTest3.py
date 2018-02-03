#
# This code obtains all groups of which Frank is a member,
# by sending an HTTP request to the Spark server
# This is really everyone, because we will go through pages
#

import requests
import json
from pprint import pprint
import os


os.system('clear')

# Let's make a class that represents a single rooms
class Room(object):
  name = ""
  isPerson = False
  id = ""
# end of class

url = "https://api.ciscospark.com/v1/rooms"
aut = "Bearer ZDY5N2FjOTctNjczZC00NGI1LWI1YzktZTRhNmQwMTlmYzhmZWI0ZDFlNjItZmUy"
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




#for room in room_list:
#  print(room.name)
