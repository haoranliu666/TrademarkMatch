use /Users/haoranliu/match/Trademark/Original_data/crsp/21jfye9kmoqem2l5.dta, clear

rename PERMNO id
rename HCOMNAM name
sort name id
by name: keep if _n==1
sort id

use /Users/haoranliu/match/Trademark/My_data/crsp/crsp.dta, replace
