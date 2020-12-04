# TMA_match

### Get data

[USPTO Trademark](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-assignment-dataset)
- 2019 Assignor DTA
- Run in stata:
```stata
keep rf_id or_name
duplicates drop
save trademark
```

[Compustat](https://wrds-web.wharton.upenn.edu/wrds/ds/comp/funda/index.cfm?navId=80)
- Step1: Fiscal year; 1950-01 to 2019-07
- Step2: GVKEY; Search the entire database; Screening Variables: all deselect Output
- Step3: Data items; Company name
- Step4: STATA v14+ file
- Run in stata:
```stata
keep gvkey conm
duplicates drop, force
save compustat
```

CRSP

CIQ subsidiary names

### Clean name
Run [trademark_name_process.py](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/trademark_name_process.py)

### Bing Search

### Match
