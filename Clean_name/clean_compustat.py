import json
import re

import pandas as pd

data = pd.read_stata('compustat.dta')
data_nodup = data.drop_duplicates('conml')

list_gvkey = list(data_nodup['gvkey'])

list_old_conm = list(data_nodup['conml'])
list_conm = []
for i in range(0, len(list_old_conm)):
    name = list_old_conm[i].lower()  # lower case
    list_conm.append(name)

# save all characters in company names
dict_clean_char = {}  # a dict, key = characters, value = [(gvkey, name), ...]
for i in range(0, len(list_gvkey)):
    name = list_conm[i]
    for char in name:
        if char != " ":
            gvkey = list_gvkey[i]
            if char not in dict_clean_char:
                dict_clean_char[char] = [(gvkey, name)]  # create new key
            else:
                dict_clean_char[char].append((gvkey, name))

list_char = list(dict_clean_char.keys())
list_char.sort()  # all characters list


# replace ., to space
for i in range(0, len(list_conm)):
    name = list_conm[i]
    if '.,' in name:
        newname = name.replace('.,', ' ')
        list_conm[i] = newname

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


for i in range(0, len(list_conm)):
    name = list_conm[i]
    newname = list_conm[i]
    for n_x in range(10, 0, -1):
        newname = fix_pattern(newname, n_x)
    if newname != name:
        list_conm[i] = newname

# replace characters using the dict
with open('dict_char_replace.json', 'r') as f:
    dict_replace = json.load(f)

list_conm_afcharc = []
for i in range(0, len(list_conm)):
    name = list_conm[i]
    newchar_list = []
    for char in name:
        if char != ' ':
            newchar_list.append(dict_replace[char])
        else:
            newchar_list.append(' ')
    newname = ''.join(newchar for newchar in newchar_list)
    list_conm_afcharc.append(newname)

# dont replace . as space, keep dot, because for .com or .net keeping them has better results for search
# dot space or dot at the end of the string or dot at beg
dot2replace_re = re.compile(r"\. |\.$|^\.")
for i in range(0, len(list_conm_afcharc)):
    name = list_conm_afcharc[i]
    newname = dot2replace_re.sub(' ', name)
    list_conm_afcharc[i] = newname

# clean extra white space
white0_re = re.compile(r" +")
for i in range(0, len(list_conm_afcharc)):
    name = list_conm_afcharc[i]
    newname = white0_re.sub(' ', name)
    list_conm_afcharc[i] = newname

# begin or end with whitespace
white1_re = re.compile(r"^ | $")
for i in range(0, len(list_conm_afcharc)):
    name = list_conm_afcharc[i]
    newname = white1_re.sub('', name)
    list_conm_afcharc[i] = newname

# take care of u s, u s a
usa_re = re.compile(r"\b(u) \b(s) \b(a)\b")
us_re = re.compile(r"\b(u) \b(s)\b")
for i in range(0, len(list_conm_afcharc)):
    name = list_conm_afcharc[i]
    newname = usa_re.sub('usa', name)
    newname = us_re.sub('us', newname)
    list_conm_afcharc[i] = newname


# json list
with open('list_compustat_gvkey.json', 'w') as handle:
    json.dump(list_gvkey, handle, indent=2)

with open('list_compustat_conml.json', 'w') as handle:
    json.dump(list_old_conm, handle, indent=2)

with open('list_compustat_newname.json', 'w') as handle:
    json.dump(list_conm_afcharc, handle, indent=2)
