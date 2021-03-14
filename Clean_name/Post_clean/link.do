*** tma assignor
cd /Users/haoranliu/match/Trademark/Clean_name/Post_clean

*rebuild data 
use "/Users/haoranliu/match/Trademark/Original_data/tma/tm_assignor.dta",clear
gen id = _n
save temp1.dta, replace

*merge
use /Users/haoranliu/match/Trademark/Clean_name/Post_clean/tma_assignor_grouped_num0.9.dta, clear

keep if name != name0
drop index name name0
merge m:1 id using temp1.dta
keep if _merge == 3
drop _merge
rename or_natlty state

rename id tempname
rename id0 id
merge 1:1 id using temp1.dta
rename id id0
rename tempname id 
keep if _merge == 3
drop _merge
rename or_natlty state0

keep id state id0 state0
keep if state == state0
drop if state == ""
drop state state0

save idcouple_tma_assignor, replace


*** tma assignee
*rebuild data 
use "/Users/haoranliu/match/Trademark/Original_data/tma/tm_assignee.dta",clear
gen id = _n
save temp2.dta, replace

*merge
use /Users/haoranliu/match/Trademark/Clean_name/Post_clean/tma_assignee_grouped_num0.9.dta, clear

keep if name != name0
drop index name name0
merge m:1 id using temp2.dta
keep if _merge == 3
drop _merge
rename ee_natlty state

rename id tempname
rename id0 id
merge 1:1 id using temp2.dta
rename id id0
rename tempname id 
keep if _merge == 3
drop _merge
rename ee_natlty state0

keep id state id0 state0
keep if state == state0
drop if state == ""
drop state state0

save idcouple_tma_assignee, replace

***tmc
use "/Users/haoranliu/match/Trademark/Original_data/tmc/owner.dta"
rename own_id id
save temp3.dta, replace

use /Users/haoranliu/match/Trademark/Clean_name/Post_clean/tmc_grouped_num0.9.dta, clear

keep if name != name0
drop index name name0
merge m:1 id using temp3.dta
keep if _merge == 3
drop _merge
rename own_nalty_state_cd nalty_state //这是啥
rename own_addr_state_cd addr_state

rename id tempname
rename id0 id
merge 1:1 id using temp3.dta
rename id id0
rename tempname id 
keep if _merge == 3
drop _merge
rename own_nalty_state_cd nalty_state0 //这是啥
rename own_addr_state_cd addr_state0

keep id nalty_state addr_state id0 nalty_state0 addr_state0
keep if nalty_state == nalty_state0
keep if addr_state == addr_state0
drop if nalty_state == ""
drop if addr_state0 == ""
drop nalty_state addr_state nalty_state0 addr_state0

save idcouple_tmc, replace
