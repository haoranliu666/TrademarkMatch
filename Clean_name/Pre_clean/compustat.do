use /Users/haoranliu/match/Trademark/Original_data/compustat/0fn_0list_compstatnames_new.dta, clear

rename fn_compustat name
rename gvkey id
keep name id
sort name id
by name: keep if _n==1

save /Users/haoranliu/match/Trademark/My_data/compustat.dta, replace

exit
