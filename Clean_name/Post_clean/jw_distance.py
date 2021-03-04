#tmc

import json
import textdistance
import pandas as pd

with open('list_tmc_newname.json', 'r') as handle:
    name0_list = json.load(handle)

with open('list_tmc_id.json', 'r') as handle:
    id0_list = json.load(handle)

#link id0 and name0
df = pd.DataFrame(name0_list, columns = ['name0'])
df['id0'] = id0_list

#sort by name0
df = df.sort_values(by=['name0'])
df.reset_index(drop=True, inplace=True)
name0_list = list(df['name0'])
id0_list = list(df['id0'])

#create name1 and id1
name1_list = []
id1_list = []
for i in range(0, (len(df)-1)):
    name0 = name0_list[i]
    for j in range(i+1, len(df)):
        name1 = name0_list[j]
        if name0 != name1:
            name1_list.append(name1)
            id1_list.append(id0_list[j])
            break

df = df.drop(index=len(df)-1)
df['name1'] = name1_list
df['id1'] = id1_list

#create distance
distance_list = []
for i in range(0, len(df)):
    name0 = name0_list[i]
    name1 = name1_list[i]
    d = textdistance.jaro_winkler(name0, name1)
    distance_list.append(d)

df['distance'] = distance_list
df = df.sort_values(by=['jw_distance'], ascending = False)
df.reset_index(drop=True, inplace=True)


#drop names
df = df.drop(columns=['name0', 'name1'])

df.to_stata('jw_distance.dta', version = 117)
