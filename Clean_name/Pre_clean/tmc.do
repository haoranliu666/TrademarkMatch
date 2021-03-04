*drop the individual owner 
drop if own_entity_cd==1
*drop companies outside US&CA
gen temp1 = 1 if own_nalty_state_cd ==""
gen temp2 = 1 if own_addr_state_cd ==""
gen temp3 = 1 if own_addr_country_cd != "US" & own_addr_country_cd != "CA"
gen temp4 = 1 if own_nalty_country_cd != "US" & own_nalty_country_cd != "CA"
drop if temp1 == 1 & temp2 == 1 & temp3 == 1 & temp4 == 1
*
sort own_name own_id
by own_name: keep if _n==1
keep own_name own_id
sort own_id
save tmc
