import os
import sys

cut_time = 9
set_len_list = [5, 10, 20, 50]
set_score_list = [1, 1, 1, 1]

os.system("python create_random_sample.py")
os.system(f"python cut_sample.py {cut_time}")

### Parallel Computing
set_len = set_len_list[0]
order = ""
for i in range(1, cut_time+1):
    order = order + f"python match.py {i} {set_len} &" + "\n"

os.system(order)

#
os.system(f"python combine_result.py {cut_time} {set_len}")

set_len = set_len_list[1]
order = ""
for i in range(1, cut_time+1):
    order = order + f"python match.py {i} {set_len} &" + "\n"

os.system(order)

#
os.system(f"python combine_result.py {cut_time} {set_len}")

set_len = set_len_list[2]
order = ""
for i in range(1, cut_time+1):
    order = order + f"python match.py {i} {set_len} &" + "\n"

os.system(order)

#
os.system(f"python combine_result.py {cut_time} {set_len}")

set_len = set_len_list[3]
order = ""
for i in range(1, cut_time+1):
    order = order + f"python match.py {i} {set_len} &" + "\n"

os.system(order)

#
os.system(f"python combine_result.py {cut_time} {set_len}")

######

import json

dict_list = []
for set_len in set_len_list:
    with open(f'matched_set{set_len}.json', 'r') as handle:
        temp = json.load(handle)
        dict_list.append(temp)

result_dict = dict_list[-1]
for name in result_dict.keys():
    for name1 in result_dict[name].keys():
        result_dict[name][name1] = 0 #initialize

for i in range(0, len(set_len_list)):
    for name in dict_list[i].keys():
        for name1 in dict_list[i][name].keys():
            result_dict[name][name1] += dict_list[i][name][name1]*set_score_list[i]

result = {}
for name, v in result_dict.items():
    max = 0
    for num in v.values():
        if num > max:
            max = num
    for name1, num in v.items():
        if num == max:
            result[name] = name1
    
with open('result.json', 'w') as handle:
    json.dump(result, handle, indent=2)
