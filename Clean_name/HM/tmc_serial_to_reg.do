use "/Users/haoranliu/match/Trademark/Original_data/tmc/case_file.dta", clear

keep serial_no registration_no 

destring, replace

sort registration_no

drop if registration_no == 0

save "/Users/haoranliu/match/Trademark/My_data/tmc_serial_to_reg.dta", replace
