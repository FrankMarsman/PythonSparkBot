import requests
import json
from pprint import pprint
import os
import FrankBot
import sys

os.system('clear')

id =  "ZDY5N2FjOTctNjczZC00NGI1LWI1YzktZTRhNmQwMTlmYzhmZWI0ZDFlNjItZmUy"

all_list = FrankBot.GetOccupiedRooms(id)
group_list = list(x for x in all_list if x.isPerson == False)

for i in range(0, len(group_list)):
  print("[" + str(i) + "] " + group_list[i].name)

print("Tot groups: " + str(len(group_list)))

group_index = int(input("Which group do you want to inspect? Index = "))

print("You chose " + group_list[group_index].name)
