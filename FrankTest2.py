#
# This code sends a message to a group
# from bot MacHans
#

import requests
import json
from pprint import pprint


url = "https://api.ciscospark.com/v1/messages";
aut = "Bearer YzUzMjMxODQtNTQ4Mi00Njc1LTk0Y2YtOGY5ZTQ5YmZiNGZhZDliZjUyMTMtOTY4";
con = "application/json; charset=utf-8";
header = {"Authorization":aut, "Content-type":con};

json_obj = {
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vYjc5YTQ3MDAtMDAxMy0xMWU4LTk2YjQtYzVlMDM2NzMzZTA5",
  "text": "Test message"
}

r = requests.post(url, json.dumps(json_obj), headers=header);
rjson = r.json( );

pprint(rjson);
