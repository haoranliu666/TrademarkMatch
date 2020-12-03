# TMA_match

### Get data
[USPTO Trademark](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-assignment-dataset)
- 2019 Assignor DTA
[Compustat](https://wrds-web.wharton.upenn.edu/wrds/ds/comp/funda/index.cfm?navId=80)
- Step1: Fiscal year; 1950-01 to 2019-07
- Step2: GVKEY; Search the entire database; Screening Variables: all deselect Output
- Step3: Data items; Company name
- Step4: STATA v14+ file
- Run in stata:
```stata
drop datadate fyear
duplicates drop, force
```
- Data form: two rows, gvkey and conm
- CRSP
- CIQ subsidiary names

### Clean data

### Bing Search

### Match
