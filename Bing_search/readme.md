# Azure Bing API

- [Official Manual](https://docs.microsoft.com/zh-cn/azure/cognitive-services/bing-web-search/overview)
- [search(web_data)](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python)
- [search return](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.searchresponse?view=azure-python)
- [web_pages(web_data.web_pages)](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.webwebanswer?view=azure-python)
- [value(web_data.web_pages.value[0])](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.webpage?view=azure-python)
- [ClientRawResponse(raw=True的 web_data)](https://docs.microsoft.com/zh-cn/python/api/msrest/msrest.pipeline.clientrawresponse?view=azure-pythonClientRawResponse)


# Step 1 Install
> pip install azure-cognitiveservices-search-websearch==2.0.0

# Step 2 Import
```python
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key.
subscription_key = "xxxxxx"

# Instantiate the client and replace with your endpoint.
client = WebSearchClient(endpoint="zzzzzz", credentials=CognitiveServicesCredentials(subscription_key))
```

# Step 3 Test
```python
# Make a request. Replace Yosemite if you'd like.
web_data = client.web.search(query="apple", count = 50)

#result count
print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

#print url
for i in range(0,len(web_data.web_pages.value)):
    print(web_data.web_pages.value[i].url)
```


### Some useful return value
```python 
#original_query
web_data.query_context.original_query

#name
web_data.web_pages.value[0].name

#url
web_data.web_pages.value[0].url

#A snippet of text from the webpage that describes its contents.
web_data.web_pages.value[0].snippet

#The last time that Bing crawled the webpage.
web_data.web_pages.value[0].date_last_crawled
```



    
    
    
    
    
