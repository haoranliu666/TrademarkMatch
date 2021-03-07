use /Users/haoranliu/match/Trademark/Original_data/tmc/owner.dta, clear

*drop the individual owner 
drop if own_entity_cd==1

*drop companies outside US&CA
gen temp1 = 1 if own_nalty_state_cd ==""
gen temp2 = 1 if own_addr_state_cd ==""
gen temp3 = 1 if own_addr_country_cd != "US" & own_addr_country_cd != "CA"
gen temp4 = 1 if own_nalty_country_cd != "US" & own_nalty_country_cd != "CA"
drop if temp1 == 1 & temp2 == 1 & temp3 == 1 & temp4 == 1

*drop duplication
keep own_name own_id
rename own_name name
rename own_id id
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/tmc/tmc.dta, replace
