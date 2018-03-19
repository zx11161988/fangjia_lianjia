import requests
from bs4 import BeautifulSoup
from MetrolineUri import Metroline

class Building:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    def __init__(self, url):
        self.uriArray = []
        session = requests.Session()
        req = session.get(url, headers=Building.headers)
        bsObj = BeautifulSoup(req.text, "html.parser")
        #print(bsObj)
        infoList = bsObj.findAll("div", class_="info")

        for info in infoList:
            build = info.findAll("a")
            for a in build:
                if (a.get("data-el") == "ershoufang"):
                    self.uriArray.append(a.get("href"))
                    print(a.get("href"))

    def getUriList(self):
        return self.uriArray



if __name__=='__main__':
    creater = Building("https://cd.lianjia.com/ditiefang/li110460718s100021801/ng1hu1nb1/")
    creater.getUriList()
