import requests
from bs4 import BeautifulSoup

class Metroline:
    prefix = "https://cd.lianjia.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    def __init__(self, url):
        self.metro_info = {}
        session = requests.Session()
        req = session.get(url, headers=Metroline.headers)
        bsObj = BeautifulSoup(req.text, "html.parser")
        metrol = bsObj.find("div", {"data-role":"ditiefang"})
        print(metrol)
        metro_href = metrol.findAll("a")
        for href in metro_href:
            print(href.get_text())
            metro_building_url = Metroline.prefix + href.get('href')
            print(metro_building_url)
            self.metro_info[href.get_text()] = metro_building_url
        for k, v in self.metro_info.items():
            print("Test: ", k, v)

    def getMetroline(self):
        return self.metro_info


if __name__ == '__main__':
    Metroline(url="https://cd.lianjia.com/ershoufang/ng1hu1nb1/")
