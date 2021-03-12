use /Users/haoranliu/match/Trademark/Original_data/crsp/0fn_0list_crspnames_new.dta, clear

*id is generated from original order of the data
gen id = _n
rename fn_crspmsf name
keep name id
sort name id
by name: keep if _n==1

save /Users/haoranliu/match/Trademark/My_data/crsp.dta, replace

exit
