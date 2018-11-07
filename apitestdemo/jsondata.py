import requests


url = "http://www.kuaidi100.com/query?type=tiantian&postid=669176849992"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }  # get方法其它加个ser-Agent就可以了

s = requests
r = s.get(url, headers=headers, verify=False)
result = r.json()
print(result['data'][0])
