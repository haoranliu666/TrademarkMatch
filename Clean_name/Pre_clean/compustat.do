use /Users/haoranliu/match/Trademark/Original_data/compustat/YUDFCDY9ELZ8ZR4G.dta, clear


keep gvkey conml
rename gvkey id
rename conml name
sort name id
by name: keep if _n==1
sort id

save /Users/haoranliu/match/Trademark/My_data/compustat/compustat.dta, replace
