import requests
from bs4 import BeautifulSoup
from MetrolineUri import Metroline

class Community:
    uriArray = ["https://cd.lianjia.com/chengjiao/ng1hu1nb1l3/"]
    prefix = "https://cd.lianjia.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    def __init__(self, url):
        session = requests.Session()
        req = session.get(url, headers=Community.headers)
        bsObj = BeautifulSoup(req.text, "html.parser")
        metrol = bsObj.find("div", {"data-role":"ditiefang"})
        print(metrol)
        self.dict_url = {}
        metro_href = metrol.findAll("a")
        for href in metro_href:
            print(href.get_text())
            if(href.get_text().find("号线") < 0):
                #self.set_url.add(Metroline.prefix + href.get("href"))
                self.dict_url[href.get_text()] = Metroline.prefix + href.get("href")
                print(href.get("href"))
        for k, v in self.dict_url.items():
            print("Test, CommunityUriGenerator: ", k, v)

    def getDictUrl(self):
        return self.dict_url


if __name__ == '__main__':
    Community(url="https://cd.lianjia.com/ditiefang/li110460718ng1hu1nb1/")
