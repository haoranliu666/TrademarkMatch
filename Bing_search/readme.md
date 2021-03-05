# Bing网页搜索API

- [官方文档](https://docs.microsoft.com/zh-cn/azure/cognitive-services/bing-web-search/overview)
- [search方法(实例 web_data)](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.operations.weboperations?view=azure-python)
- [search返回](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.searchresponse?view=azure-python)
- [web_pages方法(实例 web_data.web_pages)](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.webwebanswer?view=azure-python)
- [value方法(实例 web_data.web_pages.value[0])](https://docs.microsoft.com/zh-cn/python/api/azure-cognitiveservices-search-websearch/azure.cognitiveservices.search.websearch.models.webpage?view=azure-python)
- [ClientRawResponse(实例raw=True的 web_data)](https://docs.microsoft.com/zh-cn/python/api/msrest/msrest.pipeline.clientrawresponse?view=azure-pythonClientRawResponse)


# Step 1 安装
首先在控制台安装bing search包，要2.0.0版本，原代码采用的包为2019年的1.0.0版本，代码不兼容，需要更新
> pip install azure-cognitiveservices-search-websearch==2.0.0

# Step 2 导入
```python
#进入python环境
# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Replace with your subscription key.
subscription_key = "xxxxxx"

# Instantiate the client and replace with your endpoint.
client = WebSearchClient(endpoint="zzzzzz", credentials=CognitiveServicesCredentials(subscription_key))
```

# Step 3 测试
```python
# Make a request. Replace Yosemite if you'd like.
web_data = client.web.search(query="apple", count = 50)

#result count
print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

#print url
for i in range(0,len(web_data.web_pages.value)):
    print(web_data.web_pages.value[i].url)
```


### 一些有用的返回值
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



    
    
    
    
    
