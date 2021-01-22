from bs4 import BeautifulSoup
import requests
import pandas as pd

def Crawler_Stock(code):
    url = 'https://finance.naver.com/item/sise.nhn?code=%s' % (code)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tag = soup.find_all("td", {"class": "num"})


    result = []
    data = []
    for i in tag:
        data.append(i.text.replace('\t', '').replace('\n', ''))

    result.append(code)     # 종목코드
    result.append(data[5])  # 전일종가
    result.append(data[7])  # 시가
    result.append(data[11]) # 저가
    result.append(data[9])  # 고가
    result.append(data[0])  # 종가
    result.append(data[6])  # 거래량

    return result

code = '091120'
price = Crawler_Stock(code)
print(price)
