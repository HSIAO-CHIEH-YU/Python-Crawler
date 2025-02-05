from os import write

import requests

url="https://www.ptt.cc/bbs/Mobile-game/index.html"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
response=requests.get(url,headers=headers)
#print(response.text)
if response.status_code==200:
    with open("output.html","w",encoding="utf-8")as f:
        f.write(response.text)
    print("寫入成功")
else:
    print("寫入失敗")