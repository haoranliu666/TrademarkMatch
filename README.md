step to step guide: [steps](https://github.com/FutureMathematician/TMA_match/blob/main/steps.md)


### Time line
2021/03/14
- Bug fixes.
- Changed Post-clean totally, using TF-IDF for fuzzy matching, and using state data to make sure the matching is correct.
- Todo: finish bing_seach, and cppmatch

2021/03/09
- Added cmatch.c, try to do the match process using C instead of Python for performance improvement, still in progress.
- Known issue: CIQ clean process has bug.
- Todo: Finish cmatch.

2021/03/07
- Separeted pre-clean, clean and post-clean, to make clean process clearer.
- Known issue: CIQ clean process has bug.

2021/03/04
- Added post match process to reduce sample.
- Added [Jaro–Winkler distance](https://en.wikipedia.org/wiki/Jaro–Winkler_distance) to find paired similiar company names, majorly caused by typo. Using city name data to make sure they are the same company.
- Known Issues: City names in Case Files is nonstandard, and also have typos.

2021/02/28
- Added TMC clean process, updated all other clean processes.
- Updated dict json.
- Added combine_all_names.py
- Todo: Use string distance method reduce company name size.

2021/02/07
- Added CIQ clean process, updated compustat and tma clean process.
- Added matching process, using maximiumed weight function to define matched.
- Todo: futher step on cleaning: combine name files, reduce duplicated ones.

2021/02/03
- Added CRSP clean process.
- Replaced json to pickle for saving data in overall code.
- Added CRSP bing search process, it uses parallel computing to send multiple requests to Microsoft Azure, saves time significantly. (notice: this also means the money will run out significantly faster.)
- Added preliminary matching code, it uses parallel computing to save time.
- Todo: CIQ clean name process and matching process are still in progress.

2021/01/25
- I refactored the Clean_name code, reduced redundant clean steps, changed dict to list for restoring cleaned data.
- Known issues: some names are long because they contain an explanation of the company; some names contain strange characters like &2942, and the meaning is unknown; whether the [mapping](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/dict_char_replace.json) is optimized is still unknown
