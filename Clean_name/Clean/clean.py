import json
import re

import pandas as pd

data_name_list = ["crsp", "compustat", "ciq", "tma_assignee", "tma_assignor", "tmc"]
read_directory = "/Users/haoranliu/match/Trademark/My_data/"
save_directory = "/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/"

def clean_data(data_name):
    print(f"clean {data_name}")
    data = pd.read_stata(read_directory + data_name + ".dta")

    list_id = list(data['id'])
    list_old_name = list(data['name'])
    list_new_name = []
    for i in range(0, len(list_old_name)):
        name = list_old_name[i].lower()  # lower case
        list_new_name.append(name)

    # replace ., to space
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        if '.,' in name:
            newname = name.replace('.,', ' ')
            list_new_name[i] = newname

    # replacce x.y.z to xyz
    def fix_pattern(name, i):  # i from 10 to 1
        temp_re = re.compile(r'\b(\w)' + i*r'\.(\w)\b')  # x.x.x
        m = re.search(temp_re, name)
        if m:
            new_re = ''.join(ele for ele in ['\\' + str(j)
                                            for j in range(1, i+1+1)])
            # reverse quoation, new_re = r"\1\2\3"
            newname = temp_re.sub(new_re, name)
            return newname
        else:
            return name

    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = list_new_name[i]
        for n_x in range(10, 0, -1):
            newname = fix_pattern(newname, n_x)
        if newname != name:
            list_new_name[i] = newname

    # map through a dictionary
    with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/dict_char_replace.json', 'r') as f:
        dict_replace = json.load(f)

    list_new_name_temp = []
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newchar_list = []
        for char in name:
            if char != ' ' and char != '\x7f':
                newchar_list.append(dict_replace[char])
            else:
                newchar_list.append(' ')
        newname = ''.join(newchar for newchar in newchar_list)
        list_new_name_temp.append(newname)

    list_new_name = list_new_name_temp

    dot2replace_re = re.compile(r"\. |\.$|^\.")
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = dot2replace_re.sub(' ', name)
        list_new_name[i] = newname

    for i in range(0, len(list_new_name)):
        name0 = list_new_name[i]
        name0 = name0.replace('.ltd.', ' ltd ')
        name0 = name0.replace('.ltd', ' ltd ')
        name0 = name0.replace('ltd.', ' ltd ')
        name0 = name0.replace('.limited', ' ltd ')
        name0 = name0.replace('.inc.', ' inc ')
        name0 = name0.replace('.inc', ' inc ')
        name0 = name0.replace('inc.', ' inc ')
        name0 = name0.replace('incorporated', ' inc ')
        name0 = name0.replace('incorporation', ' inc ')
        name0 = name0.replace('.co', ' co ')
        name0 = name0.replace('co.', ' co ')
        name0 = name0.replace('company', ' co ')
        name0 = name0.replace('.llc', ' llc ')
        name0 = name0.replace('llc.', ' llc ')
        name0 = name0.replace('corp.', ' corp ')
        name0 = name0.replace('.corp', ' corp ')
        name0 = name0.replace('.corporation', ' corp ')
        name0 = name0.replace('corporation', ' corp ')
        list_new_name[i] = name0

    #limited
    white0_re = re.compile(r" limited$")
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = white0_re.sub(' ltd', name)
        list_new_name[i] = newname

    # clean extra white space
    white0_re = re.compile(r" +")
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = white0_re.sub(' ', name)
        list_new_name[i] = newname

    # begin or end with whitespace
    white1_re = re.compile(r"^ | $")
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = white1_re.sub('', name)
        list_new_name[i] = newname

    # take care of u s, u s a
    usa_re = re.compile(r"\b(u) \b(s) \b(a)\b")
    us_re = re.compile(r"\b(u) \b(s)\b")
    for i in range(0, len(list_new_name)):
        name = list_new_name[i]
        newname = usa_re.sub('usa', name)
        newname = us_re.sub('us', newname)
        list_new_name[i] = newname

    # save json list
    with open(save_directory + data_name + '_id.json', 'w') as handle:
        json.dump(list_id, handle, indent=2)

    with open(save_directory + data_name + '_oldname.json', 'w') as handle:
        json.dump(list_old_name, handle, indent=2)

    with open(save_directory + data_name + '_newname.json', 'w') as handle:
        json.dump(list_new_name, handle, indent=2)

for data_name in data_name_list:
    clean_data(data_name)