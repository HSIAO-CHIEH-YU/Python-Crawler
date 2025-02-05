import  requests
from bs4 import BeautifulSoup

url="https://www.pttweb.cc/bbs/Beauty/M.1662117340.A.71B"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
         "Cookie":"PTTweb_v2_guestId_persistent=1087385584; PTTweb_v2_authKey_persistent=thy5g16m1fyr8jee8nd45uob9a; PTTweb_v2_guestId=1087385584; PTTweb_v2_authKey=thy5g16m1fyr8jee8nd45uob9a; _ga=GA1.1.1539595487.1738739198; __gads=ID=5b756ae0f6a7d561:T=1738739198:RT=1738739198:S=ALNI_MaUkjaO3AjwD8zPCtTtIFBDZgEAjA; __gpi=UID=0000102a9c0f99f8:T=1738739198:RT=1738739198:S=ALNI_MZjfEdJS8zoAlNufJd8n52UFEGyBg; __eoi=ID=76569055266fb3b1:T=1738739198:RT=1738739198:S=AA-AfjZSzRjLtAdH4A2o8x2tqob-; _ga_F0HJ7JBSPD=GS1.1.1738739198.1.1.1738740331.0.0.0; FCNEC=%5B%5B%22AKsRol-W4Qiat_Wy-NH8H-8QemVB6OKU8rkF7zKlqmaLQhJkxLrH5vRzQfnL5uTPJvWBf8bQP4HIxjXEoErKMZFjXDjMiLJXWu7dh1CVIljG7GZCzoIQF4KcMipItGRCpTy7_lNjF-yE_zMejlHCfnwqomXQxHj8ZQ%3D%3D%22%5D%5D"}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
#print(soup.prettify())
spans=soup.find("title")#找到標題
spans2=spans.text#只保留標題文字 html格式不要
print(spans2)
