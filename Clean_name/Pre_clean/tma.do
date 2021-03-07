use /Users/haoranliu/match/Trademark/Original_data/tma/tm_assignor.dta, clear

*note: rf_id cannot identically identify the data
keep or_name rf_id
rename or_name name
rename rf_id id
sort name id
by name: keep if _n==1

save /Users/haoranliu/match/Trademark/My_data/tma/tma.dta, replace
