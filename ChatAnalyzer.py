#
# This program allows one to analyze the rooms
# that a bot is in. You can select which room to analyze
# and it will download all messages from that room
#

import requests
import json
import os
import FrankBot
import sys
import collections

from pprint import pprint
from os import path
from wordcloud import WordCloud

os.system('clear')

id = "MmM0ZTFiYTAtZThhYi00NTVlLThiYTQtODg4MmU1Yzk4MTgzZGUyZTUwMzItZDM4"
id = "ZDY5N2FjOTctNjczZC00NGI1LWI1YzktZTRhNmQwMTlmYzhmZWI0ZDFlNjItZmUy"

all_list = FrankBot.GetOccupiedRooms(id)
group_list = list(x for x in all_list if x.isPerson == False)

for i in range(0, len(group_list)):
  print("[" + str(i) + "] " + group_list[i].name)

# select group to analyze
gi = int(input("Which group do you want to inspect? Index = "))
print("You chose " + group_list[gi].name)

roomId = group_list[gi].id
msgs =  group_list[gi].GetMessages(id, roomId)
nonEmpty = []

for msg in msgs:
  if len(msg.text) > 0:
    nonEmpty.append(msg.text)


fileName = group_list[gi].name + ".txt"
file = open(fileName, "w")

for str in nonEmpty:
  file.write(str + "\n")

file.close( )

#print("Total messages: " + str(len(msgs)))


d = path.dirname("")
text = open(path.join(d, fileName)).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()













# end
