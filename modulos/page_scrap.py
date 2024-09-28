import requests 
from bs4 import BeautifulSoup

url ='http://localhost:80/'
response = requests.get(url)
raw_html = response.text

parsed_html = BeautifulSoup(raw_html,'html.parser', from_encoding='utf-8')
# print(parsed_html)
# print(parsed_html.title.text)  # type: ignore
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# print(top_jobs_heading)

article =top_jobs_heading.parent  # type: ignore
# print(article)
for p in article.select('p'):  # type: ignore
    print(p)