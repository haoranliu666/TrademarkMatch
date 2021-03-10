use /Users/haoranliu/match/Trademark/Original_data/ciq/0fn_0list_ciqnames_new.dta, clear

keep ciqsubid fn_ciqsub
rename ciqsubid id
rename fn_ciqsub name
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/ciq/ciq.dta, replace

exit
