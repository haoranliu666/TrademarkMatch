use /Users/haoranliu/match/Trademark/Original_data/ciq/0fn_0list_ciqnames.dta, clear

keep ciqsubid ciqsubid_firmname
rename ciqsubid id
rename ciqsubid_firmname name
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/ciq/ciq.dta, replace
