*temp
use "/Users/haoranliu/match/Trademark/Original_data/compustat/0fn_0list_compstatnames_new.dta", clear

destring gvkey, replace

save "/Users/haoranliu/match/Trademark/Original_data/compustat/temp.dta", replace

*main
use /Users/haoranliu/match/Trademark/Original_data/tmc/owner.dta, clear

destring serial_no, replace

merge m:1 serial_no using "/Users/haoranliu/match/Trademark/My_data/hm_serial_gvkey.dta"

keep if _merge == 3
drop _merge


merge m:1 gvkey using "/Users/haoranliu/match/Trademark/Original_data/compustat/temp.dta"
drop if _merge == 2 //个别gvkey居然没有对应项？

sort serial_no

order own_name fn_compustat serial_no own_type_cd 
