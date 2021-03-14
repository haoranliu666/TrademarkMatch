import json
import pandas as pd

data_name_list = ['tma_assignor', 'tma_assignee', 'tmc']

for data_name in data_name_list:
    grouped = pd.read_stata(f'/Users/haoranliu/match/Trademark/Clean_name/Post_clean/idcouple_{data_name}.dta')
    with open(f'/Users/haoranliu/match/Trademark/Clean_name/Post_clean/{data_name}_id.json', 'r') as handle:
        original_id = json.load(handle)
    with open(f'/Users/haoranliu/match/Trademark/Clean_name/Post_clean/{data_name}_newname.json', 'r') as handle:
        original_newname = json.load(handle)

    id_newname_dict = {}
    for i in range(0, len(original_id)):
        id_newname_dict[original_id[i]] = original_newname[i]

    temp1 = list(grouped['id'])
    temp0 = list(grouped['id0'])
    id0_id_dict = {}
    for i in range(0, len(temp0)):
        id0_id_dict[temp0[i]] = temp1[i]

    postcleaned_newname = []
    for i in range(0, len(original_id)):
        if original_id[i] in id0_id_dict.keys():
            temp_id = id0_id_dict[original_id[i]]
        else:
            temp_id = original_id[i]
        postcleaned_newname.append(id_newname_dict[temp_id])

    with open(f'/Users/haoranliu/match/Trademark/Clean_name/Post_clean/post_cleaned/{data_name}_postcleaned_newname.json', 'w') as handle:
        json.dump(postcleaned_newname, handle, indent=2)