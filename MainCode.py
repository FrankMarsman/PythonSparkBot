import requests
import json
from pprint import pprint
import os
import FrankBot
import sys
import collections

os.system('clear')

#id = "ZDY5N2FjOTctNjczZC00NGI1LWI1YzktZTRhNmQwMTlmYzhmZWI0ZDFlNjItZmUy"
id = "MmM0ZTFiYTAtZThhYi00NTVlLThiYTQtODg4MmU1Yzk4MTgzZGUyZTUwMzItZDM4"
all_list = FrankBot.GetOccupiedRooms(id)
#group_list = list(x for x in all_list if x.isPerson == False)
group_list = all_list

for i in range(0, len(group_list)):
  print("[" + str(i) + "] " + group_list[i].name)

print("Tot groups: " + str(len(group_list)))

person_list = []
for i in range(0, len(group_list)):
#for i in range(0, 10):
  temp_list = FrankBot.GetRoomOccupants(id, group_list[i].id)
  person_list.extend(temp_list)
  print("Group " + str(i) + "/" + str(len(group_list))
      + ", #Person in current group = " + str(len(temp_list))
      + ", Tot. #Persons = " + str(len(person_list)))

cnt = collections.Counter( )
for person in person_list:
  cnt[person.name] += 1

pprint(cnt)

print("#Persons in group: " + str(len(person_list)))
print("#Of unique persons: " + str(len(cnt)))


#gi = int(input("Which group do you want to inspect? Index = "))
#print("You chose " + group_list[gi].name)

#person_list = FrankBot.GetRoomOccupants(id, group_list[gi].id)

#for i in range(0, len(person_list)):
#  print("[" + str(i) + "] " + person_list[i].name + " (" + person_list[i].email + ")")
#
#print("#Persons in group: " + str(len(person_list)))
