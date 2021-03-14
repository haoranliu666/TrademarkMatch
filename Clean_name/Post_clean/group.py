import json
import pandas as pd
from string_grouper import match_strings, group_similar_strings
from datetime import datetime


data_name_list = ["crsp", "compustat", "ciq", "tma_assignee", "tma_assignor", "tmc"]
#data_name_list = ["tma_assignee", "tma_assignor", "tmc"]
#data_name_list = ["tmc"]

#for num in [0.95, 0.9, 0.85, 0.8, 0.7]:
for num in [0.9]:
    for data_name in data_name_list:
        print(f"\n{data_name} start num = {num}");
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        with open(data_name + '_newname.json', 'r') as f:
            name_list = json.load(f)

        with open(data_name + '_id.json', 'r') as f:
            id_list = json.load(f)

        df = pd.DataFrame()
        df['name'] = name_list
        df['id'] = id_list

        # matches = match_strings(master = df['name'], master_id = df['id'])#, min_similarity = 0.2)
        # matches.to_stata('aaaa.dta', version = 117)

        temp = group_similar_strings(strings_to_group = df['name'], string_ids = df['id'], min_similarity = num)
        temp['name0'] = df['name']
        temp['id0'] = df['id']
        temp.to_stata(f'{data_name}_grouped_num{num}.dta', version = 117)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

