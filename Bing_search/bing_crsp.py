import sys
import json

from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

#imput your keys "xxxxxxxxxxx"
subscription_key = "xxxxxxxx"
client = WebSearchClient(endpoint="yyyyyy", credentials=CognitiveServicesCredentials(subscription_key))

with open('list_crsp_newname.json', 'r') as handle:
    list_name = json.load(handle)  # cleaned names

# cut 100 files
task_num = int(sys.argv[1])
task_len = len(list_name)//99
if task_num <= 99:
    list_name = list_name[(task_num-1)*task_len:task_num*task_len]
elif task_num == 100:
    list_name = list_name[(task_num-1)*task_len:len(list_name)]

url_crsp = [0]*len(list_name)
for i in range(0, len(list_name)):
    url_crsp[i] = [0]*50

for i in range(0, len(list_name)):
    try:
        web_data = client.web.search(query = list_name[i], client_ip = "64.38.64.0", count = 50)
    except Exception as err:
        pass
    else:
        for j in range(0, len(web_data.web_pages.value)):
            url_crsp[i][j] = web_data.web_pages.value[j].url
    finally:
        pass

with open(f'url_crsp_{task_num}.json', 'w') as handle:
    json.dump(url_crsp, handle, indent=2)
