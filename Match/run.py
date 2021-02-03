import os
import sys

cut_time = 9
set_len_list = [5, 10, 20, 50]
set_score_list = [10, 8, 5, 3]

os.system("python create_random_sample.py")
os.system(f"python cut_sample.py {cut_time}")

set_len = set_len_list[3] #0 1 2 3 
order = ""
for i in range(1, cut_time+1):
    order = order + f"python match.py {i} {set_len} &" + "\n"

os.system(order)

os.system(f"python combine_result.py {cut_time} {set_len}")

for i in set_len:
    with open(f'matched_set{set_len}.json', 'r') as handle:
        a1 = json.load(handle)

    with open(f'matched_set{set_len}.json', 'r') as handle:
        a2 = json.load(handle)

    with open(f'matched_set{set_len}.json', 'r') as handle:
        a3 = json.load(handle)

    with open(f'matched_set{set_len}.json', 'r') as handle:
        a4 = json.load(handle)

