import requests
from bs4 import BeautifulSoup
from MetrolineUri import Metroline

class Page:
          #https://cd.lianjia.com/chengjiao/pg2ng1hu1nb1l3/
    #url = "https://cd.lianjia.com/chengjiao/ng1hu1nb1l3/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    def __init__(self, url):
        self.uriArray = []
        session = requests.Session()
        req = session.get(url, headers=Page.headers)
        bsObj = BeautifulSoup(req.text, "html.parser")
        try:
            page = bsObj.find("div", class_="page-box house-lst-page-box").attrs["page-data"]
            page_uri = bsObj.find("div", class_="page-box house-lst-page-box").attrs["page-url"]
            pagedict = eval(page)
            print(page)
            print(page_uri)
            self.totolpage = pagedict['totalPage']
            self.currentpage = pagedict['curPage']
            for i in range(self.currentpage, self.totolpage + 1):
                self.uriArray.append(Metroline.prefix + page_uri.replace("{page}", str(i)))
            for listss in list(set(self.uriArray)):
                print(listss)
        except AttributeError as e:
            print("PageUI:", e)
        else:
            self.uriArray.append(url)

    def getUriList(self):
        return self.uriArray


if __name__=='__main__':
    creater = Page("https://cd.lianjia.com/ditiefang/li1613492049948368s1613492497690008/ng1hu1nb1/")
    creater.getUriList()
