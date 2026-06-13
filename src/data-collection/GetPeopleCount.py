import requests
from bs4 import BeautifulSoup
from datetime import datetime


def GetPeopleCount():
    url = "https://winpoweryouthpark.com.tw/%E5%A0%B4%E9%A4%A8%E4%BB%8B%E7%B4%B9/%E5%81%A5%E8%BA%AB%E6%88%BF%E5%8D%80/%E5%81%A5%E8%BA%AB%E4%B8%AD%E5%BF%83/"

    response = requests.get(url, timeout=10)

    # 確認 request 成功
    response.raise_for_status()

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    counts = soup.select(".pcount")

    for item in counts:
        if "體適能中心" in item.text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            weekday = datetime.now().weekday()
            count = item.select_one(".notice").text.strip()


            return (timestamp, weekday, count)
    return None