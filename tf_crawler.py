#A simple code for crawling the information of the popular TF-lipsticks
import requests
import re
from bs4 import BeautifulSoup

url='https://www.tom-ford.cn/'
data={}
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

response=requests.get(url,headers=headers)
html_doc=response.content #TF
#print(response.status_code)   #状态码
#print(response.content.decode("utf-8")) #内容

soup=BeautifulSoup(html_doc, #html文档字符串
        'html.parser', #html解析器
        from_encoding='utf-8' #html文档编码
        )

TF_type=soup.find_all('a',href=re.compile(r"goods-"))

for tf_type in TF_type:
    #print(tf_type.name,tf_type['href'],tf_type.get_text())
    print(tf_type.get_text())
