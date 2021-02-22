# TMA_match

### Get data

[CRSP](https://wrds-web.wharton.upenn.edu/wrds//ds/crsp/stock_a/stkhdr.cfm)
- Step1: PERMNO
- Step2: Search the entire database
- Step3: Company Name Header



[Compustat](https://wrds-web.wharton.upenn.edu/wrds/ds/comp/funda/index.cfm?navId=80)
- Step1: Fiscal year; 1950-01 to 2019-07
- Step2: GVKEY; Search the entire database
- Step3: Data items; CONML
- Step4: STATA v14+ file
- Run in stata:
```stata
keep gvkey conml
duplicates drop
save compustat
```


[CIQ subsidiary names](https://www.capitaliq.com/)



[USPTO Trademark Assignment Dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-assignment-dataset)
- 2019 Assignor DTA
- Run in stata:
```stata
keep rf_id or_name
duplicates drop
save tma
```



[USPTO Trademark Case Files Dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-case-files-dataset-0)
- 2019 Owner DTA
- Run in stata:
```stata
*drop the individual owner 
drop if own_entity_cd==1 
keep own_id serial_no own_name
save tmc
```

### Clean name
Run [clean_crsp.py](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/clean_crsp.py), [clean_compustat.py](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/clean_compustat.py), [clean_ciq.py](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/clean_ciq.py), [clean_tma.py](https://github.com/FutureMathematician/TMA_match/blob/main/Clean_name/clean_tma.py).

### Bing Search

### Match
