import requests
import pandas as pd
url="https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36,"
          }
response=requests.get(url,headers=headers)
if response.status_code==200:
    data=response.json()
    #print(data["data"]["courseData"]["products"])
    products=data["data"]["courseData"]["products"]
    course_list=[]
    for product in products:
        course_data={"title":product["title"],
                     "rating":product["averageRating"],
                     "price":product["price"],
                     "number":product["numSoldTickets"]}
        #print(product["title"])#印出title
        course_list.append(course_data)
    #print(course_list)
    df=pd.DataFrame(course_list)
    df.columns=["課程標題", "評價", "售價", "已賣出"]#標題與上面給的key不同,所以要先創建好 再來重新命名欄位
    df.to_excel("HahowClass.xlsx",index=False, engine="openpyxl")