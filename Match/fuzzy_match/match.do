cd /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor

use /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_crsp0.7.dta, clear
gsort left_id -similarity
by left_id: keep if _n == 1
keep left_id right_id
save assignor_crsp_idpair.dta, replace

use /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_compustat0.7.dta, clear
gsort left_id -similarity
by left_id: keep if _n == 1
keep left_id right_id
save assignor_compustat_idpair.dta

use /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_ciq0.7.dta, clear
gsort left_id -similarity
by left_id: keep if _n == 1
keep left_id right_id
save assignor_ciq_idpair.dta

*link
use /Users/haoranliu/match/Trademark/My_data/tma_assignor.dta, clear
rename id left_id
rename name assignor_name

*crsp id = permno
merge 1:1 left_id using /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_crsp_idpair.dta
drop _merge
rename right_id id
merge m:1 id using /Users/haoranliu/match/Trademark/My_data/crsp.dta 
drop if _merge == 2
drop _merge
rename name crsp_name
merge m:1 id using /Users/haoranliu/match/Trademark/My_data/crsp_id.dta
drop if _merge == 2
drop _merge id
rename permno crsp_id

*compustat id = gvkey
merge 1:1 left_id using /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_compustat_idpair.dta
drop _merge
rename right_id id
merge m:1 id using /Users/haoranliu/match/Trademark/My_data/compustat.dta 
drop if _merge == 2
drop _merge
rename name compustat_name
rename id compustat_id

*ciq id = ciqsubid
merge 1:1 left_id using /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/assignor_ciq_idpair.dta
drop _merge
rename right_id id
merge m:1 id using /Users/haoranliu/match/Trademark/My_data/ciq.dta 
drop if _merge == 2
drop _merge
rename name ciq_name
rename id ciq_id

rename left_id assignor_id
sort assignor_id

*
count //520,141
count if (crsp_id != .) | (ciq_id != "") | (compustat_id != "") //158,133

*
keep if (crsp_id != .) | (ciq_id != "") | (compustat_id != "") 
drop *_name
gen matched_database = 0
replace matched_database = 3 if compustat_id != ""
replace matched_database = 2 if ciq_id != ""
replace matched_database = 1 if crsp_id != .
label define matched_database 1 "crsp" 2 "ciq" 3 "compustat"
label value matched_database matched_database

save /Users/haoranliu/match/Trademark/Match/fuzzymatch/tma_assignor/matched.dta, replace
