# 1. 代码解读

```python3
from bs4 import BeautifulSoup # 用于解析html和xml页面

from keybert import keyBERT # 用于提取文本关键词和关键短语

query_term = '%22' + qury_term + '%22' # 用于构建URL中查询的参数，%22是双引号“的URL编码

query_term.replace(' ', '%20') # URL查询参数中不允许直接包含空格，用%20来表示空格

bulk_data_api_url = f"https://developer.uspto.gov/ibd-api/v1/application/publications?searchText={query_term}&start={start}&largeTextSearchFlag=Y" # 用于构建一个用于查询美国专利商标局(USPTO)公共数据api的URL。https://developer.uspto.gov/ibd-api/v1/application/publications这是 USPTO 提供的公共数据API的URL，用于检索专利申请的公开信息。searchText={query_term}用于指定搜索文本。start=0表示从第一条数据开始。largeTextSearchFlag=Y指定启用大文本搜索。
```

