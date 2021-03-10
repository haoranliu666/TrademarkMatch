use /Users/haoranliu/match/Trademark/Original_data/tma/tm_assignee.dta, clear

*note: rf_id cannot identically identify the data
gen num = _n
rename ee_name name
rename num id
sort name id
by name: keep if _n==1

drop if ee_legal_entity_text == "INDIVIDUAL"

keep if ///
ee_country == "" ///
| ee_country == "UNITED STATES" ///
| ee_country == "CANADA" ///
| ee_country == "VIRGIN ISLANDS, U.S." ///
| ee_country == "GUAM"

keep if ///
ee_natlty == "" ///
| ee_natlty == "UNITED STATES" ///
| ee_natlty == "CANADA" ///
| ee_natlty == "ALABAMA" ///
| ee_natlty == "ALASKA" ///
| ee_natlty == "ARIZONA" ///
| ee_natlty == "ARKANSAS" ///
| ee_natlty == "CALIFORNIA" ///
| ee_natlty == "COLORADO" ///
| ee_natlty == "CONNECTICUT" ///
| ee_natlty == "DELAWARE" ///
| ee_natlty == "FLORIDA" ///
| ee_natlty == "GEORGIA" ///
| ee_natlty == "HAWAII" ///
| ee_natlty == "IDAHO" ///
| ee_natlty == "ILLINOIS" ///
| ee_natlty == "INDIANA" ///
| ee_natlty == "IOWA" ///
| ee_natlty == "KANSAS" ///
| ee_natlty == "KENTUCKY" ///
| ee_natlty == "LOUISIANA" ///
| ee_natlty == "MAINE" ///
| ee_natlty == "MARYLAND" ///
| ee_natlty == "MASSACHUSETTS" ///
| ee_natlty == "MICHIGAN" ///
| ee_natlty == "MINNESOTA" ///
| ee_natlty == "MISSISSIPPI" ///
| ee_natlty == "MISSOURI" ///
| ee_natlty == "MONTANA" ///
| ee_natlty == "NEBRASKA" ///
| ee_natlty == "NEVADA" ///
| ee_natlty == "NEW HAMPSHIRE" ///
| ee_natlty == "NEW JERSEY" ///
| ee_natlty == "NEW MEXICO" ///
| ee_natlty == "NEW YORK" ///
| ee_natlty == "NORTH CAROLINA" ///
| ee_natlty == "NORTH DAKOTA" ///
| ee_natlty == "OHIO" ///
| ee_natlty == "OKLAHOMA" ///
| ee_natlty == "OREGON" ///
| ee_natlty == "PENNSYLVANIA" ///
| ee_natlty == "RHODE ISLAND" ///
| ee_natlty == "SOUTH CAROLINA" ///
| ee_natlty == "SOUTH DAKOTA" ///
| ee_natlty == "TENNESSEE" ///
| ee_natlty == "TEXAS" ///
| ee_natlty == "UTAH" ///
| ee_natlty == "VERMONT" ///
| ee_natlty == "VIRGINIA" ///
| ee_natlty == "WASHINGTON" ///
| ee_natlty == "WEST VIRGINIA" ///
| ee_natlty == "WISCONSIN" ///
| ee_natlty == "WYOMING" ///
| ee_natlty == "DISTRICT OF COLUMBIA" ///
| ee_natlty == "AMERICAN SAMOA" ///
| ee_natlty == "GUAM" ///
| ee_natlty == "NORTHERN MARIANA ISLANDS" ///
| ee_natlty == "PUERTO RICO" ///
| ee_natlty == "VIRGIN ISLANDS"


keep name id
sort id

save /Users/haoranliu/match/Trademark/My_data/tma/tma_assignee.dta, replace


exit
