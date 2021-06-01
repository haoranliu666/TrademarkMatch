import json
import pandas as pd
from string_grouper import match_strings, match_most_similar, \
	group_similar_strings, compute_pairwise_similarities, \
	StringGrouper

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/tma_assignor_newname.json') as f:
	tma_assignor_name = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/tma_assignor_id.json') as f:
	tma_assignor_id = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/compustat_newname.json') as f:
	compustat_name = json.load(f)

with open('/Users/haoranliu/match/Trademark/Clean_name/Clean/cleaned/compustat_id.json') as f:
	compustat_id = json.load(f)

tma_assignor = pd.DataFrame()
tma_assignor['name'] = tma_assignor_name
tma_assignor['id'] = tma_assignor_id

compustat = pd.DataFrame()
compustat['name'] = compustat_name
compustat['id'] = compustat_id

# num = 0.9 
# matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = compustat['name'], duplicates_id = compustat['id'], min_similarity = num)
# matches.to_stata(f'assignor_compustat{num}.dta', version = 117)
# num = 0.8 
# matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = compustat['name'], duplicates_id = compustat['id'], min_similarity = num)
# matches.to_stata(f'assignor_compustat{num}.dta', version = 117)
num = 0.7 
matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = compustat['name'], duplicates_id = compustat['id'], min_similarity = num)
matches.to_stata(f'assignor_compustat{num}.dta', version = 117)
# num = 0.6
# matches = match_strings(master = tma_assignor['name'], master_id = tma_assignor['id'], duplicates = compustat['name'], duplicates_id = compustat['id'], min_similarity = num)
# matches.to_stata(f'assignor_compustat{num}.dta', version = 117)

#string_grouper.match_strings()
#(master, master_id, duplicates, duplicates_id, min_similarity)