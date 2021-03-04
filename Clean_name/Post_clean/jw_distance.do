*rebuild data 
use owner.dta, clear
drop if own_entity_cd==1
gen temp1 = 1 if own_nalty_state_cd ==""
gen temp2 = 1 if own_addr_state_cd ==""
gen temp3 = 1 if own_addr_country_cd != "US" & own_addr_country_cd != "CA"
gen temp4 = 1 if own_nalty_country_cd != "US" & own_nalty_country_cd != "CA"
drop if temp1 == 1 & temp2 == 1 & temp3 == 1 & temp4 == 1
sort own_name own_id
by own_name: keep if _n==1
keep own_addr_1 own_addr_2 own_addr_city own_id
save temp.dta

*merge
use jw_distance.dta, clear
drop index
rename id0 own_id
merge 1:1 own_id using temp.dta
keep if _merge == 3
drop _merge
rename own_id id0
rename own_addr_1 own_addr_1_0
rename own_addr_2 own_addr_2_0
rename own_addr_city own_addr_city_0

rename id1 own_id
merge m:1 own_id using temp.dta
keep if _merge == 3
drop _merge
rename own_id id1
rename own_addr_1 own_addr_1_1
rename own_addr_2 own_addr_2_1
rename own_addr_city own_addr_city_1

*check distance
gsort -distance
gen flag = 1
replace own_addr_2_0= lower(own_addr_2_0)
replace own_addr_2_1= lower(own_addr_2_1)
replace own_addr_1_0= lower(own_addr_1_0)
replace own_addr_1_1= lower(own_addr_1_1)
replace own_addr_city_0= lower(own_addr_city_0)
replace own_addr_city_1= lower(own_addr_city_1)
replace flag = -1 if own_addr_2_0 != own_addr_2_1
replace flag = -2 if own_addr_1_0 != own_addr_1_1
replace flag = -3 if own_addr_city_0 != own_addr_city_1
replace flag = -4 if own_addr_1_0 == "" & own_addr_2_0 == "" & own_addr_city_0 == ""

*count flag
count if flag == 1
count if flag == -1
count if flag == -2
count if flag == -3
count if flag == -4

save final
