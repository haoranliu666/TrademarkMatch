use /Users/haoranliu/match/Trademark/Original_data/crsp/0fn_0list_crspnames_new.dta, clear


gen num = _n
rename num id
rename fn_crspmsf name
keep id name
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/crsp/crsp.dta, replace

exit
