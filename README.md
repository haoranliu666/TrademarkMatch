step to step guide: [steps](https://github.com/FutureMathematician/TMA_match/blob/main/steps.md)


### Time line

2021/02/03
- Added CRSP clean process.
- Replaced json to pickle for saving data in overall code.
- Added CRSP bing search process, it uses parallel computing to send multiple requests to Microsoft Azure, saves time significantly. (notice: this also means the money will run out significantly faster.)
- Added preliminary matching code, it uses parallel computing to save time.
- Known issues: CIQ clean name process and matching process are still in progress.

2021/01/25
- I refactored the Clean_name code, reduced redundant clean steps, changed dict to list for restoring cleaned data.
- Known issues: some names are long because they contain an explanation of the company; some names contain strange characters like &2942, and the meaning is unknown; whether the [mapping](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/dict_char_replace.json) is optimized is still unknown
