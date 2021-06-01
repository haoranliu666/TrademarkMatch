import json
import pandas as pd
from string_grouper import match_strings, match_most_similar, \
	group_similar_strings, compute_pairwise_similarities, \
	StringGrouper

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/tma_assignor_newname.json') as f:
	tma_assignor_name = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/tma_assignor_id.json') as f:
	tma_assignor_id = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/crsp_newname.json') as f:
	crsp_name = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/crsp_id.json') as f:
	crsp_id = json.load(f)

tma_assignor = pd.DataFrame()
tma_assignor['name'] = tma_assignor_name
tma_assignor['id'] = tma_assignor_id

crsp = pd.DataFrame()
crsp['name'] = crsp_name
crsp['id'] = crsp_id

# num = 0.9 #12018
# # matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
# # matches.to_stata(f'assignor_crsp{num}.dta', version = 117)
# num = 0.8 #26809
# matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
# matches = match_strings(master = crsp['name'], master_id = crsp['id'], duplicates = tma_assignor['name'], duplicates_id = tma_assignor['id'], min_similarity = num)
# matches.to_stata(f'assignor_crsp{num}.dta', version = 117)
num = 0.7 #106902
matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
matches.to_stata(f'assignor_crsp{num}.dta', version = 117)
#num = 0.6 #497379
# matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
matches.to_stata(f'assignor_crsp{num}.dta', version = 117)

#string_grouper.match_strings()
#(master, master_id, duplicates, duplicates_id, min_similarity)