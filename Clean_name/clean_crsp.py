import json
import re

import pandas as pd

data = pd.read_stata('crsp.dta')
data_nodup = data.drop_duplicates('HCOMNAM')

list_id = list(data_nodup['PERMNO'])
list_old_conm = list(data_nodup['HCOMNAM'])
list_conm = []
for i in range(0, len(list_old_conm)):
    name = list_old_conm[i].lower()  # lower case
    list_conm.append(name)

list_conm_afcharc = list_conm

# pickle list
with open('list_crsp_permno.json', 'w') as handle:
    json.dump(list_id, handle, indent=2)

with open('list_crsp_hcomnam.json', 'w') as handle:
    json.dump(list_old_conm, handle, indent=2)

with open('list_crsp_newname.json', 'w') as handle:
    json.dump(list_conm_afcharc, handle, indent=2)
