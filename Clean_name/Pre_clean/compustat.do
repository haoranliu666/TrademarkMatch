use /Users/haoranliu/match/Trademark/Original_data/compustat/0fn_0list_compstatnames_new.dta, clear


keep gvkey fn_compustat
rename gvkey id
rename fn_compustat name
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/compustat/compustat.dta, replace

exit
