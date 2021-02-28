import json

data_name_list = ["crsp", "compustat", "ciq", "trademark", "tmc"]
data_list = []
for i in range(0, len(data_name_list)):
    with open(f'list_{data_name_list[i]}_newname.json', 'r') as handle:
        temp = json.load(handle)
        data_list.append(temp)

data_set_list = []
for data in data_list:
    data_set_list.append(set(data))

# create data set
data_nodup = data_set_list[0] | data_set_list[1] | data_set_list[2] | data_set_list[3] | data_set_list[4]

# change set to list
all_name = list(data_nodup)
all_name.sort()

with open('all_name.json', 'w') as handle:
    json.dump(temp, handle, indent=2)