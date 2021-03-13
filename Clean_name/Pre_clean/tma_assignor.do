use /Users/haoranliu/match/Trademark/Original_data/tma/tm_assignor.dta, clear

*id is generated from original order of the data
gen id = _n
rename or_name name

drop if or_legal_entity_text == "INDIVIDUAL"

keep if ///
or_country == "" ///
| or_country == "UNITED STATES" ///
| or_country == "CANADA" ///
| or_country == "VIRGIN ISLANDS, U.S." ///
| or_country == "GUAM"

keep if ///
or_natlty == "" ///
| or_natlty == "UNITED STATES" ///
| or_natlty == "CANADA" ///
| or_natlty == "ALABAMA" ///
| or_natlty == "ALASKA" ///
| or_natlty == "ARIZONA" ///
| or_natlty == "ARKANSAS" ///
| or_natlty == "CALIFORNIA" ///
| or_natlty == "COLORADO" ///
| or_natlty == "CONNECTICUT" ///
| or_natlty == "DELAWARE" ///
| or_natlty == "FLORIDA" ///
| or_natlty == "GEORGIA" ///
| or_natlty == "HAWAII" ///
| or_natlty == "IDAHO" ///
| or_natlty == "ILLINOIS" ///
| or_natlty == "INDIANA" ///
| or_natlty == "IOWA" ///
| or_natlty == "KANSAS" ///
| or_natlty == "KENTUCKY" ///
| or_natlty == "LOUISIANA" ///
| or_natlty == "MAINE" ///
| or_natlty == "MARYLAND" ///
| or_natlty == "MASSACHUSETTS" ///
| or_natlty == "MICHIGAN" ///
| or_natlty == "MINNESOTA" ///
| or_natlty == "MISSISSIPPI" ///
| or_natlty == "MISSOURI" ///
| or_natlty == "MONTANA" ///
| or_natlty == "NEBRASKA" ///
| or_natlty == "NEVADA" ///
| or_natlty == "NEW HAMPSHIRE" ///
| or_natlty == "NEW JERSEY" ///
| or_natlty == "NEW MEXICO" ///
| or_natlty == "NEW YORK" ///
| or_natlty == "NORTH CAROLINA" ///
| or_natlty == "NORTH DAKOTA" ///
| or_natlty == "OHIO" ///
| or_natlty == "OKLAHOMA" ///
| or_natlty == "OREGON" ///
| or_natlty == "PENNSYLVANIA" ///
| or_natlty == "RHODE ISLAND" ///
| or_natlty == "SOUTH CAROLINA" ///
| or_natlty == "SOUTH DAKOTA" ///
| or_natlty == "TENNESSEE" ///
| or_natlty == "TEXAS" ///
| or_natlty == "UTAH" ///
| or_natlty == "VERMONT" ///
| or_natlty == "VIRGINIA" ///
| or_natlty == "WASHINGTON" ///
| or_natlty == "WEST VIRGINIA" ///
| or_natlty == "WISCONSIN" ///
| or_natlty == "WYOMING" ///
| or_natlty == "DISTRICT OF COLUMBIA" ///
| or_natlty == "AMERICAN SAMOA" ///
| or_natlty == "GUAM" ///
| or_natlty == "NORTHERN MARIANA ISLANDS" ///
| or_natlty == "PUERTO RICO" ///
| or_natlty == "VIRGIN ISLANDS"

keep name id
sort name id
by name: keep if _n==1

save /Users/haoranliu/match/Trademark/My_data/tma_assignor.dta, replace

exit
