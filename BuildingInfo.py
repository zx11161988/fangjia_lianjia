import requests
from bs4 import BeautifulSoup
from MetrolineUri import Metroline

class BuildingInfo:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

    def __init__(self, url):
        self.building_info_dict = {"小区名称": "", "户型": "", "方位": "", "面积": "", "总价": "",
                         "均价": "", "楼层": "", "装修": "", "建造时间": "", "区域": "", "挂牌时间":"", "url": ""}
        self.building_info_dict['url'] = url
        session = requests.Session()
        req = session.get(url, headers=BuildingInfo.headers, timeout=3)
        bsObj = BeautifulSoup(req.text, "html.parser")
        build_name = bsObj.find("a", class_="info")
        print("name：", build_name.get_text())
        self.building_info_dict["小区名称"] = build_name.get_text()
        build_base = bsObj.findAll("div", class_="mainInfo")
        for base in build_base:
            print(base.get_text())
        self.building_info_dict["户型"] = build_base[0].get_text()
        self.building_info_dict["方位"] = build_base[1].get_text()
        self.building_info_dict["面积"] = build_base[2].get_text()
        build_price_total = bsObj.find("span", class_="total")
        print("totalprice：", build_price_total.get_text())
        self.building_info_dict["总价"] = build_price_total.get_text()
        build_unit_price = bsObj.find("span", class_="unitPriceValue")
        print(build_unit_price.get_text())
        self.building_info_dict["均价"] = build_unit_price.get_text()
        build_time = bsObj.findAll("div", class_="subInfo")
        print("time", build_time)
        self.building_info_dict["楼层"] = build_time[0].get_text()
        self.building_info_dict["装修"] = build_time[1].get_text()
        self.building_info_dict["建造时间"] = build_time[2].get_text()
        build_area = bsObj.findAll("div", class_="areaName")
        self.building_info_dict["区域"] = (build_area[0].findAll("span", class_="info")[0].get_text())
        for area in build_area[0].findAll("span", class_="info"):
            print(area.get_text())
        build_update_time = bsObj.find("div", class_="transaction").li
        print(build_update_time.findAll("span"))
        self.building_info_dict["挂牌时间"] = (build_update_time.findAll("span")[1].get_text())
        for k, v in self.building_info_dict.items():
            print("Test: ", k, v)

    def getInfoDict(self):
        return self.building_info_dict



if __name__=='__main__':
    creater = BuildingInfo("https://cd.lianjia.com/ershoufang/106100238555.html")
    creater.getInfoDict()
