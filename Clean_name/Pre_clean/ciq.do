use /Users/haoranliu/match/Trademark/Original_data/ciq/0fn_0list_ciqnames_new.dta, clear

rename fn_ciqsub name
rename ciqsubid id
keep name id
sort name id
by name: keep if _n==1

save /Users/haoranliu/match/Trademark/My_data/ciq.dta, replace

exit
