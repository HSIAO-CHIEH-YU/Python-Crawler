import  requests
from bs4 import BeautifulSoup
import  os

def download_img(url,save_path):#下載圖片
    print(f"正在下載圖片:{url}")
    #模仿使用者
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
    response=requests.get(url,headers=headers)#假裝使用者然後用requests來取得url的內容
    with open(save_path,"wb")as file:#wb寫入二進位 因為是圖片
        file.write(response.content)
    print("-"*30)

def main():
    url="https://www.ptt.cc/bbs/Mobile-game/M.1570249701.A.877.html"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
             "Cookie":"_gid=GA1.2.112255453.1738733955; _gat=1; _ga=GA1.1.1796970974.1738645809; cf_clearance=3mpy7SR.uu9b..s.vRTKLfiKdGRltA2zWrpXtuMLn1I-1738813319-1.2.1.1-4LRgRW_ZS1kDqAJSD7LzEpdChe0AsY5lAATUDmczVW_TQKJZX..yOASz2vnMe02RVSDjaLfV3N23sh8bBefKdr9Q0ecxjVQxKF8QxiSPJJHHRakVtAWP6I_DbhMxc9plUskhL.BUsqoiJ.dq8Hn2Fc_jQgywB2cES3RlE.emoqp1X8cqiq.Cfg8Kyv7GLjntrRe9REfGdBUXIFKEJgWp1qfRrLJfojRFlxnasI.yYsvqQEIG_7LIJf5JnmAOtYON5ib0SX5eXddU.aFkNZRUTpI4ZFJXDqvEdcszmKGPqFA; _ga_DZ6Y3BY9GW=GS1.1.1738812271.4.1.1738813323.0.0.0",
             "Referer":"https://www.ptt.cc/"}#Referer假裝從ppt進入到頁面
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    #print(soup.prettify())
    spans=soup.find("title")#找到標題
    title=spans.text#只保留標題文字 html格式不要
    #print(title)

    #建立資料夾
    dir_name=f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    #儲存圖片
    links=soup.find_all("a")#找連結
    allow_file_name=["jpg","png","jpeg","gif"]#要找的檔案格式
    for link in links:
        href=link.get("href")
        if not href:#如果不是連結 就跳出迴圈
            continue
        file_name=href.split("/")[-1]#圖片的檔名以/後做檔名
        extension=href.split(".")[-1].lower()#找出所有連結的檔案格式
        if extension in allow_file_name:
            print(f"檔案型態:{extension}")
            print(f"url:{href}")
            download_img(href,f"{dir_name}/{file_name}")

        #print(href)
if __name__=="__main__":
    main()