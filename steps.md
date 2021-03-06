# TMA_match

> Needed Softwares & Packages:
> 
> Python 3.8.5
>
> Anaconda 4.9.2
>
> Stata 16.1
>
> [Textdistance 4.2.1](https://pypi.org/project/textdistance/)
>
> [Azure-cognitiveservices-search-websearch 2.0.0](https://pypi.org/project/azure-cognitiveservices-search-websearch/)




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

[CIQ subsidiary names](https://www.capitaliq.com/)

[USPTO Trademark Assignment Dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-assignment-dataset)
- 2019 Assignor DTA

[USPTO Trademark Case Files Dataset](https://www.uspto.gov/learning-and-resources/electronic-data-products/trademark-case-files-dataset-0)
- 2019 Owner DTA

### Clean name
Run [.do files](https://github.com/FutureMathematician/TMA_match/tree/main/Clean_name/Pre_clean) in stata

Run [.py files](https://github.com/FutureMathematician/TMA_match/tree/main/Clean_name/clean) using python3.8 with anaconda 4.8.3
### Bing Search

### Match
