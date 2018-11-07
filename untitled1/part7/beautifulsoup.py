'''
beatifulSoup是一个可以从html或xml文件提取数据的一个python库
pip insall beautifulsoup4
'''
from bs4 import BeautifulSoup
import re
html_doc = "D://pytest//untitled1//part7//PythonPO.html"
html_file = open(html_doc, "r", encoding="UTF-8")
html_handle = html_file.read()
soup = BeautifulSoup(html_handle, 'html.parser')
#print(soup)

#获取html文档头
print(soup.head)
#获取html文档中p标签
print(soup.p)
#获取加点属性
print(soup.p.attrs)
#获取所有p标签
ps= soup.find_all("p")
#id定位
result = soup.find_all(id="xxx")
#按css搜索
jobs = soup.find_all("td", class_= "jobs")   #td标签下class为jobs的

#与正则结合
names= soup.find_all("a", calss_="turnno")  #a标签下class=turnno表示名字
r = re.findall(">(.)</a>", str(names))  #在找出的结果中，正则匹配>和</a>之间的内容