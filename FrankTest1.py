#
# This code obtains all groups of which Frank is a member,
# by sending an HTTP request to the Spark server
# Also, it counts the number of converstations with people
#

import requests
import json
from pprint import pprint


url = "https://api.ciscospark.com/v1/rooms";
aut = "Bearer ZDY5N2FjOTctNjczZC00NGI1LWI1YzktZTRhNmQwMTlmYzhmZWI0ZDFlNjItZmUy";
r = requests.get(url, headers={"Authorization":aut});
rjson = r.json( );
pplCounter = 0;

for room in rjson["items"]:
  if room["type"] == "direct":
    print(room["title"]);
    pplCounter = pplCounter + 1;

print("User is in " + str(pplCounter) + " rooms that are one on one.")
